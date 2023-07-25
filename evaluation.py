from utils.images import *
from utils.datasets import *
from detectors import *
from evaluation.scrg_bsf import *
from evaluation.roc_cruve import *
from evaluation.my_pd_fa import *
from evaluation.pd_fa import *

from tqdm import tqdm
import scipy.io as scio

if __name__ == '__main__':
    algorithms = [Tophat]
    # algorithms = [LCM, MaxMedian, MPCM, PSTNN, IPI]
    # datasets = [MDFA, SIRST, NUDTSIRST, IRSTD1K, sirst_aug]
    datasets = [IRSTD1K, sirst_aug]

    dataset_dirs = {MDFA: r'./data/MDFA',
                    SIRST: r'./data/sirst',
                    NUDTSIRST: r'./data/NUDT-SIRST',
                    IRSTD1K: r'./data/IRSTD-1K',
                    sirst_aug: r'./data/sirst_aug'
                    }

    for algorithm in algorithms:
        for dataset in datasets:
            print('...Evaluating algorithm: %s, Dataset: %s' % (algorithm.__name__, dataset.__name__))

            data = dataset(base_dir=dataset_dirs[dataset])
            alg = algorithm()

            bsf_scrg = BSF_SCRG()
            roc = ROCMetric()
            eval_PD_FA = PD_FA()
            eval_my_PD_FA = my_PD_FA()

            tbar = tqdm(range(data.__len__()))
            for i in tbar:
                img, mask = data.__getitem__(i)
                alg.process(img)
                rst = alg.result['target']

                bsf_scrg.update(pred=rst, label=mask, in_img=img)
                roc.update(pred=rst, label=mask)
                eval_PD_FA.update(preds=rst, labels=mask, size=rst.shape)
                eval_my_PD_FA.update(pred=rst, label=mask)

                scrg, bsf = bsf_scrg.get()
                fpr, tpr, auc = roc.get()
                tbar.set_description('SCR_Gain: %.6f, BSF: %.6f, AUC: %.6f' % (scrg, bsf, auc))

            # Get evaluation metric results
            scrg, bsf = bsf_scrg.get()
            fpr, tpr, auc = roc.get()

            pd, fa = eval_PD_FA.get()
            pd_our, fa_our = eval_my_PD_FA.get()


            # Save results
            save_path = r'result/%s/'%(dataset.__name__)
            save_name = '%s_%s.mat' % (algorithm.__name__, dataset.__name__)
            save_dict = {'scrg': scrg,
                         'bsf': bsf,
                         'fpr': fpr,
                         'tpr': tpr,
                         'auc': auc,
                         'pd': pd,
                         'fa': fa,
                         'our_pd': pd_our,
                         'our_fa': fa_our,
                         }

            scio.savemat(osp.join(save_path, save_name), save_dict)