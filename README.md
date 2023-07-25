# ISTD-python
Codebase of model-driven Infrared Small Targets Detection (ISTD) approaches.


## Benchmark

### Background Suppression (BS)-based Methods

<table class="MsoTableGrid" border="1" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border:none;mso-border-alt:solid white .5pt;
 mso-border-themecolor:background1;mso-yfti-tbllook:1184;mso-padding-alt:0cm 5.4pt 0cm 5.4pt;
 mso-border-insideh:.5pt solid white;mso-border-insideh-themecolor:background1;
 mso-border-insidev:.5pt solid white;mso-border-insidev-themecolor:background1">
 <tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes">
  <td width="85" valign="top" style="width:63.7pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;mso-border-alt:solid white .5pt;mso-border-themecolor:
  background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Dataset</span></p>
  </td>
  <td width="294" colspan="7" valign="top" style="width:220.25pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;border-left:none;mso-border-left-alt:solid white .5pt;
  mso-border-left-themecolor:background1;mso-border-alt:solid white .5pt;
  mso-border-themecolor:background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">NUDT-SIRST</span></p>
  </td>
  <td width="294" colspan="7" valign="top" style="width:220.35pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;border-left:none;mso-border-left-alt:solid white .5pt;
  mso-border-left-themecolor:background1;mso-border-alt:solid white .5pt;
  mso-border-themecolor:background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">IRSTD-1K</span></p>
  </td>
  <td width="294" colspan="7" valign="top" style="width:220.35pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;border-left:none;mso-border-left-alt:solid white .5pt;
  mso-border-left-themecolor:background1;mso-border-alt:solid white .5pt;
  mso-border-themecolor:background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">sirst_aug</span></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:1">
  <td width="85" valign="top" style="width:63.7pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;border-top:none;mso-border-top-alt:solid white .5pt;
  mso-border-top-themecolor:background1;mso-border-alt:solid white .5pt;
  mso-border-themecolor:background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Method</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">SCRG</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">BSF</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">AUC</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Pd</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Fa</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">ourPd</span></span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">ourFa</span></span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">SCRG</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">BSF</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">AUC</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Pd</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Fa</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">ourPd</span></span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">ourFa</span></span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">SCRG</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">BSF</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">AUC</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Pd</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Fa</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">ourPd</span></span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">ourFa</span></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:2">
  <td width="85" valign="top" style="width:63.7pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;border-top:none;mso-border-top-alt:solid white .5pt;
  mso-border-top-themecolor:background1;mso-border-alt:solid white .5pt;
  mso-border-themecolor:background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">Tophat</span></span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">66.62</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">20.89</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.9994</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">91.217</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">75.738</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">96.085</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">74.860</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">60.57</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">18.70</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.9968</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">65.204</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">69.583</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">78.114</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">70.164</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">5.59</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">69.56</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.9999</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">81.155</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">16.032</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">94.911</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">11.573</span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:3">
  <td width="85" valign="top" style="width:63.7pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;border-top:none;mso-border-top-alt:solid white .5pt;
  mso-border-top-themecolor:background1;mso-border-alt:solid white .5pt;
  mso-border-themecolor:background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Fast
  <span class="SpellE">Salincy</span></span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">62.50</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">244.45</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.9911</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">55.450</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">278.618</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">59.788</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">280.229</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">114.55</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">345.14</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.9971</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">52.038</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">38.090</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">62.290</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">37.797</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">2.80</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">283.99</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.9677</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">51.857</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">913.257</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">62.861</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">913.018</span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:4;mso-yfti-lastrow:yes">
  <td width="85" valign="top" style="width:63.7pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;border-top:none;mso-border-top-alt:solid white .5pt;
  mso-border-top-themecolor:background1;mso-border-alt:solid white .5pt;
  mso-border-themecolor:background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">MaxMedian</span></span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">130.46</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">42.57</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.9992</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">84.868</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">30.407</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">93.757</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">28.231</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">138.77</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">45.87</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.9943</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">71.160</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">13.883</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">82.155</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">14.232</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">10.50</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">148.62</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.9928</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">79.367</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">7.907</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">93.535</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">4.729</span></p>
  </td>
 </tr>
</tbody></table>

### Human Visual System (HVS)-based Methods

<table class="MsoTableGrid" border="1" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border:none;mso-border-alt:solid white .5pt;
 mso-border-themecolor:background1;mso-yfti-tbllook:1184;mso-padding-alt:0cm 5.4pt 0cm 5.4pt;
 mso-border-insideh:.5pt solid white;mso-border-insideh-themecolor:background1;
 mso-border-insidev:.5pt solid white;mso-border-insidev-themecolor:background1">
 <tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes">
  <td width="85" valign="top" style="width:63.7pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;mso-border-alt:solid white .5pt;mso-border-themecolor:
  background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Dataset</span></p>
  </td>
  <td width="294" colspan="7" valign="top" style="width:220.25pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;border-left:none;mso-border-left-alt:solid white .5pt;
  mso-border-left-themecolor:background1;mso-border-alt:solid white .5pt;
  mso-border-themecolor:background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">NUDT-SIRST</span></p>
  </td>
  <td width="294" colspan="7" valign="top" style="width:220.35pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;border-left:none;mso-border-left-alt:solid white .5pt;
  mso-border-left-themecolor:background1;mso-border-alt:solid white .5pt;
  mso-border-themecolor:background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">IRSTD-1K</span></p>
  </td>
  <td width="294" colspan="7" valign="top" style="width:220.35pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;border-left:none;mso-border-left-alt:solid white .5pt;
  mso-border-left-themecolor:background1;mso-border-alt:solid white .5pt;
  mso-border-themecolor:background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">sirst_aug</span></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:1">
  <td width="85" valign="top" style="width:63.7pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;border-top:none;mso-border-top-alt:solid white .5pt;
  mso-border-top-themecolor:background1;mso-border-alt:solid white .5pt;
  mso-border-themecolor:background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Method</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">SCRG</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">BSF</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">AUC</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Pd</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Fa</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">ourPd</span></span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">ourFa</span></span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">SCRG</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">BSF</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">AUC</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Pd</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Fa</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">ourPd</span></span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">ourFa</span></span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">SCRG</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">BSF</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">AUC</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Pd</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Fa</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">ourPd</span></span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">ourFa</span></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:2">
  <td width="85" valign="top" style="width:63.7pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;border-top:none;mso-border-top-alt:solid white .5pt;
  mso-border-top-themecolor:background1;mso-border-alt:solid white .5pt;
  mso-border-themecolor:background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">LCM</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">NaN</span></span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">NaN</span></span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.6643</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">51.640</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">24119.382</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">80.952</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">24413.602</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">NaN</span></span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">NaN</span></span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.7244</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">61.442</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">8722.300</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">75.758</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">8762.480</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">NaN</span></span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">NaN</span></span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.07630</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">17.882</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">7591.351</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">29.298</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">7632.665</span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:3">
  <td width="85" valign="top" style="width:63.7pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;border-top:none;mso-border-top-alt:solid white .5pt;
  mso-border-top-themecolor:background1;mso-border-alt:solid white .5pt;
  mso-border-themecolor:background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">HB-MLCM</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">2.39</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.022</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.8901</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">1.481</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">162.692</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">1.376</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">164.509</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.53</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.025</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.8990</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.627</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">70.741</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">1.010</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">70.954</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.15</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.026</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.9771</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">1.238</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">98.815</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">3.164</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">99.188</span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:4;mso-yfti-lastrow:yes">
  <td width="85" valign="top" style="width:63.7pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;border-top:none;mso-border-top-alt:solid white .5pt;
  mso-border-top-themecolor:background1;mso-border-alt:solid white .5pt;
  mso-border-themecolor:background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">MPCM</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">108.06</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">6.70</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.9955</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">89.947</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">175.704</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">93.545</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">206.266</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">79.68</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">13.29</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.9963</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">90.909</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">52.525</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">96.296</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">58.660</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">12.96</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">22.58</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.9923</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">94.223</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">24.778</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">97.937</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">20.249</span></p>
  </td>
 </tr>
</tbody></table>

### Optimization-based Methods

<table class="MsoTableGrid" border="1" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border:none;mso-border-alt:solid white .5pt;
 mso-border-themecolor:background1;mso-yfti-tbllook:1184;mso-padding-alt:0cm 5.4pt 0cm 5.4pt;
 mso-border-insideh:.5pt solid white;mso-border-insideh-themecolor:background1;
 mso-border-insidev:.5pt solid white;mso-border-insidev-themecolor:background1">
 <tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes">
  <td width="85" valign="top" style="width:63.7pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;mso-border-alt:solid white .5pt;mso-border-themecolor:
  background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Dataset</span></p>
  </td>
  <td width="294" colspan="7" valign="top" style="width:220.25pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;border-left:none;mso-border-left-alt:solid white .5pt;
  mso-border-left-themecolor:background1;mso-border-alt:solid white .5pt;
  mso-border-themecolor:background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">NUDT-SIRST</span></p>
  </td>
  <td width="294" colspan="7" valign="top" style="width:220.35pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;border-left:none;mso-border-left-alt:solid white .5pt;
  mso-border-left-themecolor:background1;mso-border-alt:solid white .5pt;
  mso-border-themecolor:background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">IRSTD-1K</span></p>
  </td>
  <td width="294" colspan="7" valign="top" style="width:220.35pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;border-left:none;mso-border-left-alt:solid white .5pt;
  mso-border-left-themecolor:background1;mso-border-alt:solid white .5pt;
  mso-border-themecolor:background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">sirst_aug</span></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:1">
  <td width="85" valign="top" style="width:63.7pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;border-top:none;mso-border-top-alt:solid white .5pt;
  mso-border-top-themecolor:background1;mso-border-alt:solid white .5pt;
  mso-border-themecolor:background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Method</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">SCRG</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">BSF</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">AUC</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Pd</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Fa</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">ourPd</span></span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">ourFa</span></span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">SCRG</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">BSF</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">AUC</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Pd</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Fa</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">ourPd</span></span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">ourFa</span></span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">SCRG</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">BSF</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">AUC</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Pd</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Fa</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">ourPd</span></span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">ourFa</span></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:2">
  <td width="85" valign="top" style="width:63.7pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;border-top:none;mso-border-top-alt:solid white .5pt;
  mso-border-top-themecolor:background1;mso-border-alt:solid white .5pt;
  mso-border-themecolor:background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">IPI</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">267.67</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">170.41</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.9914</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">87.302</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">10.895</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">95.344</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">5.574</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">151.15</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">117.77</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.9982</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">68.652</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">6.674</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">83.165</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">6.413</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">NaN</span></span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Inf</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.9814</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">75.791</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">10.130</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">94.635</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">3.355</span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:3;mso-yfti-lastrow:yes">
  <td width="85" valign="top" style="width:63.7pt;border:solid white 1.0pt;
  mso-border-themecolor:background1;border-top:none;mso-border-top-alt:solid white .5pt;
  mso-border-top-themecolor:background1;mso-border-alt:solid white .5pt;
  mso-border-themecolor:background1;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">PSTNN</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Inf</span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Inf</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.9318</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">68.042</span></p>
  </td>
  <td width="35" valign="top" style="width:25.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">22.213</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">74.392</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">21.406</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">NaN</span></span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Inf</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.9258</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">57.994</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">8.869</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">70.370</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">7.745</span></p>
  </td>
  <td width="48" valign="top" style="width:35.9pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">NaN</span></span></p>
  </td>
  <td width="36" valign="top" style="width:27.1pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Inf</span></p>
  </td>
  <td width="41" valign="top" style="width:31.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">0.8902</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">58.597</span></p>
  </td>
  <td width="35" valign="top" style="width:25.95pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">9.206</span></p>
  </td>
  <td width="51" valign="top" style="width:38.0pt;border-top:none;border-left:none;
  border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">79.917</span></p>
  </td>
  <td width="49" valign="top" style="width:36.45pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;mso-border-bottom-themecolor:background1;
  border-right:solid white 1.0pt;mso-border-right-themecolor:background1;
  mso-border-top-alt:solid white .5pt;mso-border-top-themecolor:background1;
  mso-border-left-alt:solid white .5pt;mso-border-left-themecolor:background1;
  mso-border-alt:solid white .5pt;mso-border-themecolor:background1;padding:
  0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">3.245</span></p>
  </td>
 </tr>
</tbody></table>

## Notes
