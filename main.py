from test import *

'''4.1 Расчёт интенсивности нагрузки от абонентов фрагмента ГТС с коммутацией каналов'''
ATC_2_3_intense = ATC_2_3[1] * a_kv + ATC_2_3[2] * a_nx + ATC_2_3[3] * a_t
ATC_4_5_intense = ATC_4_5[1] * a_kv + ATC_4_5[2] * a_nx + ATC_4_5[3] * a_t
ATC_6_7_intense = ATC_6_7[1] * a_kv + ATC_6_7[2] * a_nx + ATC_6_7[3] * a_t

# Суммарная интенсивность исходящей нагрузки от всех АТСЭ
A_kk_isch = ATC_2_3_intense + ATC_4_5_intense + ATC_6_7_intense

# Интенсивность исходящей от АТСЭ нагрузки к УСС
A_ats_2_3_ycc = ATC_2_3_intense * 0.03
A_ats_4_5_yss = ATC_4_5_intense * 0.03
A_ats_6_7_yss = ATC_6_7_intense * 0.03

# Интенсивности поступающей нагрузки на ЗУС и СПСС от всех АТС
A_ats_2_3_zys = ATC_2_3[0] * a_zys
A_ats_4_5_zys = ATC_4_5[0] * a_zys
A_ats_6_7_zys = ATC_6_7[0] * a_zys

A_ats_2_3_spss_2g = A_ats_2_3_spss_4g = ATC_2_3[0] * a_spss * 0.5
A_ats_4_5_spss_2g = A_ats_4_5_spss_4g = ATC_4_5[0] * a_spss * 0.5
A_ats_6_7_spss_2g = A_ats_6_7_spss_4g = ATC_6_7[0] * a_spss * 0.5

'''4.2 Расчёт интенсивности поступающей нагрузки от абонентов MSAN'''
# -------------------------------------------MSAN 1-------------------------------------------
# Расчёт интенсивности нагрузки на MSAN 1, создаваемой абонентами с аналоговыми телефонными аппаратами:
A_ata_MSAN_1 = a_ata * MSAN_1

# Расчёт интенсивности нагрузки на MSAN1 от абонентов с телефонными аппаратами SIP и от абонентов LAN:
A_sip_MSAN_1 = a_sip * (n_LAN * N_LAN + N_sip_MSAN_1)

# Интенсивность исходящей нагрузки от сетей доступа, с учётом среднего использования существующих исходящих и входящих СЛ
A_v_5_2_MSAN_1 = n_v_5_2 * n_E1_v_5_2 * n_ock * n_isch

# Количество абонентов, включенных в сети доступа
N_v_5_2_MSAN_1 = A_v_5_2_MSAN_1 * (1 / a_ata)

# Суммарная нагрузка, поступающая на MSAN1 от абонентов всех категорий мультисервисной сети
A_MSAN_1_isch = A_ata_MSAN_1 + A_sip_MSAN_1 + A_v_5_2_MSAN_1

# Доля нагрузки, создаваемой абонентами SIP, в исходящей нагрузке составляет
k_sip_MSAN_1 = A_sip_MSAN_1 / A_MSAN_1_isch

# -------------------------------------------MSAN 2-------------------------------------------

# Расчёт интенсивности поступающей нагрузки на MSAN2 от абонентов с аналоговыми телефонными аппаратами
A_ata_MSAN_2 = a_ata * MSAN_2

# Расчёт интенсивности поступающей нагрузки на MSAN2 от абонентов с телефонными аппаратами SIP:
A_sip_MSAN_2 = N_sip_MSAN_2 * a_sip

# Интенсивность исходящей нагрузки от УПАТС, подключенных по доступу PRI, с учётом среднего использования существующих СЛ
A_pri_MSAN_2 = n_E1_upats * n_upats * n_isch * n_ock

# Количество абонентов, включенных в УПАТС
N_upats = A_pri_MSAN_2 / a_upats

# Суммарная нагрузка, поступающая на MSAN2 от абонентов всех категорий
A_MSAN_2_isch = A_ata_MSAN_2 + A_pri_MSAN_2 + A_sip_MSAN_2

# Доля нагрузки, создаваемой абонентами SIP, в исходящей нагрузке MSAN2
k_sip_MSAN_2 = A_sip_MSAN_2 / A_MSAN_2_isch

# Суммарная интенсивность исходящей нагрузки от абонентов фрагмента сети с коммутацией пакетов
A_KP_isch = A_MSAN_1_isch + A_MSAN_2_isch

# ------------------------------Интенсивность нагрузки от MSAN к УCC---------------------------

# Нагрузка в направлении к УСС для каждого MSAN составляет 3% от исходящей нагрузки:
A_MSAN_1_ycc = 0.03 * A_MSAN_1_isch
A_MSAN_2_ycc = 0.03 * A_MSAN_2_isch

# ----------------Интенсивность исходящей нагрузки от абонентов MSAN к ЗУС и СПСС--------------

N_MSAN_1 = MSAN_1 + N_v_5_2_MSAN_1 + N_sip_MSAN_1 + n_LAN * N_LAN
N_MSAN_2 = MSAN_2 + N_upats + N_sip_MSAN_2

# Интенсивность исходящей нагрузки от MSAN1 к ЗУС
A_MSAN_1_zys = N_MSAN_1 * a_zys

# Интенсивность нагрузки от MSAN2 к ЗУС:
A_MSAN_2_zys = N_MSAN_2 * a_zys

# Интенсивность нагрузки к СПСС от MSAN1 составит
A_MSAN_1_spss = N_MSAN_1 * a_spss
A_MSAN_1_spss_2g = A_MSAN_1_spss_4g = A_MSAN_1_spss / 2

# Интенсивность нагрузки к СПСС от MSAN2 составит
A_MSAN_2_spss = N_MSAN_2 * a_spss
A_MSAN_2_spss_2g = A_MSAN_2_spss_4g = A_MSAN_2_spss / 2

# Суммарная интенсивность исходящей и входящей нагрузок между MSAN1, MSAN2 и ЗУСМгМн, поступающих на MGW
A_MSAN_zys_MGW = (A_MSAN_1_zys + A_MSAN_2_zys) * 2

# Емкость проектируемого фрагмента МСС
N_MCC = N_MSAN_1 + N_MSAN_2

'''4.3 Распределение интенсивности исходящей нагрузки'''
# Суммарная интенсивность исходящей нагрузки на проектируемой сети
A_gts_isch = A_kk_isch + A_MSAN_1_isch + A_MSAN_2_isch

# Произведем распределение интенсивности исходящей нагрузки для всех АТС
A_2_3_2_3 = ATC_2_3_intense * (ATC_2_3_intense / A_gts_isch)  # АТС - 2 3
A_2_3_4_5 = ATC_2_3_intense * (ATC_4_5_intense / A_gts_isch)  # АТС - 2 3
A_2_3_6_7 = ATC_2_3_intense * (ATC_6_7_intense / A_gts_isch)  # АТС - 2 3
A_2_3_MSAN_1 = ATC_2_3_intense * (A_MSAN_1_isch / A_gts_isch)  # АТС - 2 3
A_2_3_MSAN_2 = ATC_2_3_intense * (A_MSAN_2_isch / A_gts_isch)  # АТС - 2 3

A_4_5_2_3 = ATC_4_5_intense * (ATC_2_3_intense / A_gts_isch)  # АТС - 4 5
A_4_5_4_5 = ATC_4_5_intense * (ATC_4_5_intense / A_gts_isch)  # АТС - 4 5
A_4_5_6_7 = ATC_4_5_intense * (ATC_6_7_intense / A_gts_isch)  # АТС - 4 5
A_4_5_MSAN_1 = ATC_4_5_intense * (A_MSAN_1_isch / A_gts_isch)  # АТС - 4 5
A_4_5_MSAN_2 = ATC_4_5_intense * (A_MSAN_2_isch / A_gts_isch)  # АТС - 4 5

A_6_7_2_3 = ATC_6_7_intense * (ATC_2_3_intense / A_gts_isch)  # АТС - 6 7
A_6_7_4_5 = ATC_6_7_intense * (ATC_4_5_intense / A_gts_isch)  # АТС - 6 7
A_6_7_6_7 = ATC_6_7_intense * (ATC_6_7_intense / A_gts_isch)  # АТС - 6 7
A_6_7_MSAN_1 = ATC_6_7_intense * (A_MSAN_1_isch / A_gts_isch)  # АТС - 6 7
A_6_7_MSAN_2 = ATC_6_7_intense * (A_MSAN_2_isch / A_gts_isch)  # АТС - 6 7

A_MSAN_1_MSAN_1 = A_MSAN_1_isch * (A_MSAN_1_isch / A_gts_isch)  # MSAN_1
A_MSAN_1_MSAN_2 = A_MSAN_1_isch * (A_MSAN_2_isch / A_gts_isch)  # MSAN_1
A_MSAN_2_MSAN_2 = A_MSAN_2_isch * (A_MSAN_2_isch / A_gts_isch)  # MSAN_2
A_MSAN_2_MSAN_1 = A_MSAN_2_isch * (A_MSAN_1_isch / A_gts_isch)  # MSAN_2

sum_gor_2_3 = sum([A_2_3_2_3, A_2_3_4_5, A_2_3_6_7, A_2_3_MSAN_1, A_2_3_MSAN_2])
sum_gor_4_5 = sum([A_4_5_2_3, A_4_5_4_5, A_4_5_6_7, A_4_5_MSAN_1, A_4_5_MSAN_2])
sum_gor_6_7 = sum([A_6_7_2_3, A_6_7_4_5, A_6_7_6_7, A_6_7_MSAN_1, A_6_7_MSAN_2])

'''4.4. Расчёт интенсивности нагрузки от абонентов СПСС'''
# Число абонентов N СПСС 2G и 4
N_spss_2g = N_gts - people_2G
N_spss_4g = N_gts - people_4G

# Интенсивность исходящей нагрузки от абонентов СПСС
A_spss_2g_isch = N_spss_2g * a_ssp_isch
A_spss_4g_isch = N_spss_4g * a_ssp_isch

# Интенсивность входящей нагрузки к абонентам СПСС
A_spss_2g_vhod = N_spss_2g * a_ssp_vch
A_spss_4g_vhod = N_spss_4g * a_ssp_vch

# Интенсивность входящей нагрузки к абонентам СПСС от абонентов фрагмента сети с КК
A_atce_spss_2g_vhod = sum([A_ats_2_3_spss_2g, A_ats_4_5_spss_2g, A_ats_6_7_spss_2g])
A_atce_spss_4g_vhod = sum([A_ats_2_3_spss_4g, A_ats_4_5_spss_4g, A_ats_6_7_spss_4g])

k_vhod_2_g = A_atce_spss_2g_vhod / A_spss_2g_vhod
k_vhod_4_g = A_atce_spss_4g_vhod / A_spss_4g_vhod

k_vhod_atce_2_3_spss_2g = A_ats_2_3_spss_2g / A_spss_2g_vhod
k_vhod_atce_4_5_spss_2g = A_ats_4_5_spss_2g / A_spss_2g_vhod
k_vhod_atce_6_7_spss_2g = A_ats_6_7_spss_2g / A_spss_2g_vhod

# Входящая нагрузка к абонентам СПСС от абонентов MSAN1 и MSAN2
k_vhod_MSAN_1_spss_2g = k_vhod_MSAN_1_spss_4g = A_MSAN_1_spss_2g / A_spss_2g_vhod
k_vhod_MSAN_2_spss_2g = k_vhod_MSAN_2_spss_4g = A_MSAN_2_spss_2g / A_spss_2g_vhod

# Интенсивность нагрузки от абонентов СПСС к УСС примем 3% от исходящей нагрузки
A_spss_2g_ycc = A_spss_4g_ycc = 0.03 * A_spss_2g_isch
A_spss_2g_zys_isch = A_spss_4g_zys_isch = a_zys * N_spss_2g

# Интенсивность исходящей и входящей нагрузок на участках СПСС-ЗУС
A_spss_2g_zys = A_spss_4g_zys = A_spss_2g_zys_isch * 2

# Интенсивность нагрузки на направлении MGW – ЗУСЭ
A_MGW_zys = A_spss_4g_zys + A_MSAN_zys_MGW

# Суммарная входящая нагрузка от абонентов АТСЭ и MSAN к абонентам СПСС4G и абонентам СПСС2G равна
A_atce_MSAN_spss_4g = A_atce_MSAN_spss_2g = A_atce_spss_4g_vhod + A_MSAN_1_spss_4g + A_MSAN_2_spss_4g

# Интенсивность входящей нагрузки от абонентов СПСС4G к абонентам СПСС2G к абонентам СПСС4G и к абонентам СПСС2G
A_spss_4g_to_spss_2g = A_spss_4g_vhod - A_atce_MSAN_spss_4g
k_vhod_spss_spss = A_spss_4g_to_spss_2g / A_spss_4g_vhod
A_spss_2g_spss_4g_vhod = A_spss_4g_spss_2g_vhod = A_spss_4g_to_spss_2g / 2

# Интенсивность исходящей нагрузки от абонентов СПСС распределим в соответствии с долями входящей нагрузки
A_spss_2g_isch_atce = A_spss_4g_isch_atce = k_vhod_2_g * A_spss_2g_isch
A_spss_2g_isch_atce_2_3 = k_vhod_atce_2_3_spss_2g * A_spss_2g_isch
A_spss_2g_isch_atce_4_5 = k_vhod_atce_4_5_spss_2g * A_spss_2g_isch
A_spss_2g_isch_atce_6_7 = k_vhod_atce_6_7_spss_2g * A_spss_2g_isch

A_spss_2g_isch_MSAN_1 = A_spss_4g_isch_MSAN_1 = k_vhod_MSAN_1_spss_2g * A_spss_2g_isch
A_spss_2g_isch_MSAN_2 = A_spss_4g_isch_MSAN_2 = k_vhod_MSAN_2_spss_2g * A_spss_2g_isch

SUM_zys = sum([A_ats_2_3_zys, A_ats_4_5_zys, A_ats_6_7_zys, A_MSAN_1_zys, A_MSAN_2_zys])
SUM_spss_2 = sum([A_spss_2g_isch_atce_2_3 * 2, A_spss_2g_isch_atce_4_5 * 2, A_spss_2g_isch_atce_6_7 * 2, A_spss_2g_isch_MSAN_1 * 2, A_spss_2g_isch_MSAN_2 * 2])
SUM_spss_2g = sum([A_spss_2g_isch_atce_2_3, A_spss_2g_isch_atce_4_5, A_spss_2g_isch_atce_6_7, A_spss_2g_isch_MSAN_1, A_spss_2g_isch_MSAN_2])
SUM_spss_4g = sum([A_spss_2g_isch_atce_2_3, A_spss_2g_isch_atce_4_5, A_spss_2g_isch_atce_6_7, A_spss_2g_isch_MSAN_1, A_spss_2g_isch_MSAN_2])

# Интенсивность исходящей нагрузки от абонентов СПСС2G к абонентам СПСС2G и к абонентам СПСС4G, а также от абонентов СПСС4G к абонентам СПСС4G и к абонентам СПСС2G
A_spss_2g_spss_2g_isch = A_spss_2g_spss_4g_isch = A_spss_4g_spss_2g_isch = A_spss_4g_spss_4g_isch = (A_spss_2g_isch - SUM_spss_4g) / 2

'''4.5 Расчёт числа цифровых соединительных линий (каналов) на направлениях межстанционной связи'''
