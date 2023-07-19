from utils.images import *
from utils.datasets import *
from detectors import *
from evaluation.scrg_bsf import *
from evaluation.roc_cruve import *

from tqdm import tqdm
import scipy.io as scio

if __name__ == '__main__':
    algorithms = [LCM]
    datasets = [MDFA, SIRST]

    dataset_dirs = {MDFA: r'./data/MDFA',
                    SIRST: r'./data/sirst'}

    for algorithm in algorithms:
        for dataset in datasets:
            print('...Evaluating algorithm: %s, Dataset: %s' % (algorithm.__name__, dataset.__name__))

            data = dataset(base_dir=dataset_dirs[dataset])
            alg = algorithm()

            bsf_scrg = BSF_SCRG()
            roc = ROCMetric()

            tbar = tqdm(range(data.__len__()))
            for i in tbar:
                img, mask = data.__getitem__(i)
                alg.process(img)
                rst = alg.result['target']

                bsf_scrg.update(pred=rst, label=mask, in_img=img)
                roc.update(pred=rst, label=mask)

                scrg, bsf = bsf_scrg.get()
                fpr, tpr, auc = roc.get()
                tbar.set_description('SCR_Gain: %.6f, BSF: %.6f, AUC: %.6f' % (scrg, bsf, auc))

            # Get evaluation metric results
            scrg, bsf = bsf_scrg.get()
            fpr, tpr, auc = roc.get()

            # Save results
            save_path = r'result/'
            save_name = '%s_%s.mat' % (algorithm.__name__, dataset.__name__)
            save_dict = {'scrg': scrg,
                         'bsf': bsf,
                         'fpr': fpr,
                         'tpr': tpr,
                         'auc': auc}

            scio.savemat(osp.join(save_path, save_name), save_dict)