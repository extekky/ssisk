from tabulate import tabulate
from main import *

TABLE_TYPE = 'orgtbl'
data = [
    ['Интенсивность исходящей нагрузки', 'АТСЭ-2,3', 'АТСЭ-4,5', 'АТСЭ-6,7', 'ВСЕГО'],
    ['От абонентов АТСЭ к абонентам АТСЭ и MSAN', ATC_2_3_intense, ATC_4_5_intense, ATC_6_7_intense, A_kk_isch],
    ['От АТСЭ к УСС', A_ats_2_3_ycc, A_ats_4_5_yss, A_ats_6_7_yss, sum([A_ats_2_3_ycc, A_ats_4_5_yss, A_ats_6_7_yss])],
    ['От АТСЭ к ЗУС', A_ats_2_3_zys, A_ats_4_5_zys, A_ats_6_7_zys, sum([A_ats_2_3_zys, A_ats_4_5_zys, A_ats_6_7_zys])],
    ['От АТСЭ к СПСС 2G', A_ats_2_3_spss_2g, A_ats_4_5_spss_2g, A_ats_6_7_spss_2g, sum([A_ats_2_3_spss_2g, A_ats_4_5_spss_2g, A_ats_6_7_spss_2g])],
    ['От АТСЭ к СПСС 4G', A_ats_2_3_spss_4g, A_ats_4_5_spss_4g, A_ats_6_7_spss_4g, sum([A_ats_2_3_spss_4g, A_ats_4_5_spss_4g, A_ats_6_7_spss_4g])]
]

print('Таблица 4.1')
print(tabulate(data, headers='firstrow', tablefmt=TABLE_TYPE))


data = [
    ['Интенсивность нагрузки', 'MSAN 1', 'MSAN2'],
    ['Суммарная исходящая нагрузка от абонентов MSAN', A_MSAN_1_isch, A_MSAN_2_isch],
    ['Исходящая нагрузка к ЗУС', A_MSAN_1_zys, A_MSAN_2_zys],
    ['Исходящая нагрузка к СПСС 2G', A_MSAN_1_spss_2g, A_MSAN_2_spss_2g],
    ['Исходящая нагрузка к СПСС 4G', A_MSAN_1_spss_4g, A_MSAN_2_spss_4g],
    ['Нагрузка к УСС', A_MSAN_1_ycc, A_MSAN_2_ycc]
]

print('\n\nТаблица 4.2')
print(tabulate(data, headers='firstrow', tablefmt=TABLE_TYPE))


data = [
    ['Объекты ГТС', 'Емкость'],
    ['АТСЭ-2,3', ATC_2_3[0]],
    ['АТСЭ-4,5', ATC_4_5[0]],
    ['АТСЭ-6,7', ATC_6_7[0]],
    ['Проектируемые MSAN 1 и MSAN 2', N_MCC]
]

print('\n\nТаблица 4.3')
print(tabulate(data, headers='firstrow', tablefmt=TABLE_TYPE))


data = [
    ['Номер объекта', 'АТСЭ-2,3', 'АТСЭ-4,5','АТСЭ-6,7','MSAN 1', 'MSAN 2', 'Σ', 'ЗУС', 'СПСС 2G', 'СПСС 4G', 'УСС'],
    ['АТСЭ-2,3',A_2_3_2_3, A_2_3_4_5, A_2_3_6_7, A_2_3_MSAN_1, A_2_3_MSAN_2, sum_gor_2_3, A_ats_2_3_zys, A_ats_2_3_spss_2g, A_ats_2_3_spss_2g, A_ats_2_3_ycc],
    ['АТСЭ-4,5', A_4_5_2_3, A_4_5_4_5, A_4_5_6_7, A_4_5_MSAN_1, A_4_5_MSAN_2, sum_gor_4_5, A_ats_4_5_zys, A_ats_4_5_spss_2g, A_ats_4_5_spss_2g, A_ats_4_5_yss],
    ['АТСЭ-6,7', A_6_7_2_3, A_6_7_4_5, A_6_7_6_7, A_6_7_MSAN_1, A_6_7_MSAN_2, sum_gor_6_7, A_ats_6_7_zys, A_ats_6_7_spss_2g, A_ats_6_7_spss_2g, A_ats_6_7_yss],
    ['MSAN1', A_2_3_MSAN_1, A_4_5_MSAN_1, A_6_7_MSAN_1, '?', '?','?', A_MSAN_1_zys, A_MSAN_1_spss_2g, A_MSAN_1_spss_2g, A_MSAN_1_ycc],
    ['MSAN2', A_2_3_MSAN_2, A_4_5_MSAN_2, A_6_7_MSAN_2, '?', '?','?', A_MSAN_2_zys, A_MSAN_2_spss_4g, A_MSAN_2_spss_4g,A_MSAN_2_ycc],
    ['Σ', sum_gor_2_3, sum_gor_4_5, sum_gor_6_7],
    ['ЗУС', A_ats_2_3_zys, A_ats_4_5_zys, A_ats_6_7_zys, A_MSAN_1_zys, A_MSAN_2_zys, SUM_zys],
    ['СПСС', A_spss_2g_isch_atce_2_3 * 2, A_spss_2g_isch_atce_4_5 * 2, A_spss_2g_isch_atce_6_7 * 2, A_spss_2g_isch_MSAN_1 * 2, A_spss_2g_isch_MSAN_2 * 2, SUM_spss_2],
    ['СПСС2G', A_spss_2g_isch_atce_2_3, A_spss_2g_isch_atce_4_5, A_spss_2g_isch_atce_6_7, A_spss_2g_isch_MSAN_1, A_spss_2g_isch_MSAN_2, SUM_spss_2g],
    ['СПСС4G', A_spss_2g_isch_atce_2_3, A_spss_2g_isch_atce_4_5, A_spss_2g_isch_atce_6_7, A_spss_2g_isch_MSAN_1, A_spss_2g_isch_MSAN_2, SUM_spss_4g],

]

print('\n\nТаблица 4.4')
print(tabulate(data, headers='firstrow', tablefmt=TABLE_TYPE))
