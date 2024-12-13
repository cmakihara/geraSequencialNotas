import os

'''
:gerarSequencial: Gera a sequencia de numeros entre as faixas informadas
:param faixaNotas: Lista de faixa inicial e final
:output: os numeros sequencias entra as faixa inicial e final
''' 
def gerarSequencial(faixaNotas):
    qtdNotas=0
    if(len(faixaNotas)%2 == 0):
        for i in range(0,len(faixaNotas),2):
            ini = faixaNotas[i]
            fim = faixaNotas[i+1]
            if ini > fim:
                print('ALERTA: Contem faixa inicial menor que a final Verifique\n')
                print('Faixa inicial: ',ini,'\nFaixa final: ',fim,'\n')
                input('Press ENTER to exit') 
                exit()

            while(ini <= fim):
                print(ini, end =",")
                ini += 1
                qtdNotas +=1
        print("\n\nTotal de numerações de notas geradas: ",qtdNotas,'\n')        
        input('Press ENTER to exit')    
    else:
        print("ERRO: QTD IMPAR das faixas de notas\n")
        #inserirFaixas()

       
def inserirFaixas():    
    faixaNotas = faixaInput.split(',') 
    os.system('cls')
    for faixa in faixaNotas:
        if not(faixa.isnumeric()):
            print("ERRO somente (numero) e (,) permitido\n")
            print('Caractere invalido: ',faixa,'\n')
            input('Press ENTER to exit')   
            exit()
    
    listNotas = list(map(int,faixaNotas))
    gerarSequencial(listNotas)

faixaInput = '3428,3428,3430,3437,3575,3575,3603,3603,3652,3652,3691,3691,3911,3911,3934,3934,4010,4021,4069,4069,4193,4193,4262,4262,4299,4299,4979,4985,5267,5268,5808,5809,5822,5822,5942,5942,6105,6105,6230,6230,6232,6232,6436,6436,6455,6455,6873,6873,9582,9582,13438,13438,13441,13441,13465,13465,17211,17211,19493,19493,19988,19988,20032,20032,20130,20130,20222,20222,20408,20408,21444,21451,21454,21454,21456,21456,21458,21458,21460,21460,21462,21463,21466,21466,21468,21468,21470,21472,21475,21476,21480,21480,21482,21484,21486,21486,21488,21489,21491,21492,21494,21495,21498,21503,21505,21505,21507,21511,21513,21514,21516,21532,21534,21537,21540,21540,21542,21545,21549,21549,21551,21556,21558,21560,21562,21563,21565,21572,21574,21578,21582,21583,21585,21586,21588,21588,21590,21590,21596,21600,21602,21606,21608,21609,21611,21621,21625,21630,21633,21637,21640,21641,21643,21643,21646,21646,21648,21648,21650,21651,21653,21657,21659,21661,21663,21667,21669,21670,21672,21675,21678,21678,21680,21681,21686,21690,21692,21699,21701,21704,21706,21707,21710,21714,21721,21722,21724,21724,21729,21735,21737,21745,21747,21760,21762,21762,21764,21766,21768,21771,21773,21777,21780,21780,21782,21782,21788,21788,21790,21791,21793,21794,21796,21804,21806,21809,21811,21816,21818,21820,21822,21824,21826,21826,21829,21833,21835,21837,21840,21848,21850,21852,21854,21855,21857,21858,21860,21860,21862,21864,21866,21867,21869,21872,21875,21887,21889,21891,21893,21896,21899,21900,21902,21902,21906,21906,21912,21915,21917,21918,21921,21921,21923,21924,21926,21926,21928,21928,21930,21931,21934,21934,21936,21940,21942,21943,21945,21947,21950,21954,21956,21959,21961,21966,21969,21972,21976,21977,21979,21980,21987,21987,21997,21998,22000,22000,22003,22003,22009,22009,22011,22011,22013,22013,22017,22017,22019,22019,22021,22023,22026,22026,22028,22030,22033,22033,22036,22036,22040,22042,22047,22054,22056,22057,22059,22061,22065,22068,22070,22071,22073,22079,22083,22083,22086,22094,22096,22098,22100,22100,22102,22103,22105,22108,22110,22110,22112,22113,22115,22115,22117,22119,22122,22126,22128,22134,22136,22136,22139,22142,22147,22150,22153,22155,22157,22164,22166,22166,22169,22170,22172,22173,22178,22182,22187,22191,22193,22194,22199,22199,22203,22207,22209,22210,22212,22212,22214,22214,22216,22216,22220,22220,22222,22229,22231,22231,22233,22236,22239,22240,22243,22247,22249,22250,22252,22252,22254,22255,22261,22262,22264,22268,22271,22271,22273,22275,22277,22278,22280,22281,22284,22288,22290,22291,22293,22296,22299,22301,22303,22303,22305,22309,22313,22316,22318,22319,22321,22324,22326,22327,22330,22331,22333,22338,22341,22341,22343,22343,22345,22346,22348,22348,22350,22351,22354,22354,22356,22356,22358,22359,22361,22361,22363,22364,22366,22367,22369,22369,22371,22385,22387,22387,22389,22393,22398,22402,22405,22405,22407,22407,22410,22410,22412,22412,22414,22414,22417,22425,22427,22429,22433,22433,22436,22436,22438,22442,22446,22448,22450,22451,22453,22460,22462,22462,22464,22465,22468,22468,22470,22476,22478,22478,22480,22483,22485,22485,22487,22488,22490,22494,22497,22498,22500,22502,22508,22510,22512,22516,22518,22521,22525,22529,22532,22532,22535,22537,22541,22543,22546,22547,22549,22551,22553,22557,22559,22559,22562,22567,22569,22570,22574,22576,22584,22585,22587,22587,22589,22593,22595,22597,22599,22600,22602,22603,22606,22608,22610,22610,22612,22614,22616,22620,22622,22625,22627,22628,22631,22632,22634,22637,22639,22639,22641,22641,22643,22644,22646,22646,22650,22653,22655,22659,22663,22663,22665,22666,22668,22669,22671,22675,22679,22686,22688,22693,22695,22695,22698,22698,22701,22702,22704,22704,22706,22712,22714,22714,22716,22719,22725,22729,22731,22735,22737,22739,22741,22741,22745,22752,22754,22755,22760,22760,22762,22766,22768,22768,22770,22770,22772,22772,22775,22777,22779,22780,22783,22787,22791,22798,22801,22801,22803,22803,22805,22806,22808,22809,22811,22813,22815,22818,22821,22821,22825,22825,22827,22828,22831,22835,22839,22839,22841,22841,22843,22844,22847,22848,22850,22851,22853,22853,22856,22856,22858,22859,22861,22862,22871,22871,22873,22877,22880,22881,22884,22884,22891,22894,22896,22897,22899,22900,22904,22907,22909,22909,22911,22913,22915,22919,22921,22921,22924,22925,22927,22932,22937,22937,22941,22941,22944,22944,22948,22948,22950,22950,22952,22955,22957,22958,22961,22962,22964,22964,22966,22968,22971,22972,22975,22976,22981,22982,22984,22988,22990,22990,22993,22995,22998,22998,23000,23000,23002,23006,23008,23019,23021,23021,23023,23026,23028,23029,23034,23043,23045,23075,23077,23077,23080,23086,23089,23091,23094,23095,23097,23097,23099,23099,23101,23101,23103,23104,23107,23113,23115,23115,23117,23133,23138,23141,23144,23145,23147,23151,23153,23156,23158,23164,23168,23169,23171,23171,23173,23173,23175,23177,23179,23179,23181,23190,23193,23193,23195,23195,23198,23200,23202,23202,23204,23206,23208,23209,23213,23219,23222,23230,23232,23232,23234,23234,23238,23239,23241,23247,23249,23249,23251,23254,23257,23258,23260,23260,23262,23267,23276,23279,23281,23283,23285,23287,23290,23294,23297,23298,23303,23307,23321,23334,23337,23337,23339,23342,23344,23351,23354,23354,23356,23362,23364,23369,23371,23372,23375,23378,23380,23380,23382,23383,23391,23394,23399,23399,23401,23403,23406,23406,23408,23410,23413,23421,23423,23423,23425,23426,23429,23429,23434,23434,23436,23439,23442,23443,23448,23451,23454,23454,23456,23466,23468,23477,23479,23483,23485,23486,23488,23490,23493,23494,23496,23497,23502,23505,23509,23514,23516,23518,23520,23522,23524,23525,23527,23534,23536,23540,23542,23542,23544,23545,23550,23550,23568,23568,23570,23570,23572,23572,23576,23592,23596,23601,23603,23604,23606,23608,23612,23612,23614,23616,23618,23619,23621,23622,23624,23624,23627,23629,23631,23634,23636,23640,23643,23645,23647,23647,23651,23651,23655,23655,23657,23661,23663,23666,23669,23674,23676,23678,23680,23680,23682,23685,23687,23687,23711,23712,23715,23716,23719,23720,23722,23724,23726,23728,23730,23734,23736,23740,23742,23745,23748,23749,23751,23751,23753,23758,23761,23763,23765,23769,23771,23776,23778,23779,23782,23784,23786,23787,23789,23794,23796,23796,23798,23804,23807,23808,23811,23811,23813,23818,23820,23822,23824,23825,23827,23831,23834,23837,23839,23839,23841,23847,23849,23852,23854,23856,23858,23859,23864,23864,23868,23868,23870,23876,23878,23878,23880,23880,23882,23882,23885,23886,23891,23891,23893,23895,23897,23907,23909,23912,23914,23914,23917,23918,23921,23928,23930,23936,23943,23943,23945,23949,23951,23952,23954,23954,23956,23957,23959,23960,23962,23964,23966,23967,23970,23970,23973,23981,23987,23988,23990,23992,23994,23995,23998,24000,24004,24004,24006,24006,24010,24013,24015,24017,24020,24023,24025,24028,24031,24032,24034,24035,24037,24039,24041,24042,24045,24046,24048,24048,24050,24056,24059,24070,24073,24074,24078,24083,24085,24088,24090,24090,24093,24093,24096,24101,24103,24103,24108,24111,24115,24119,24121,24121,24123,24125,24127,24127,24131,24134,24137,24137,24139,24139,24142,24150,24152,24153,24156,24160,24162,24174,24176,24178,24183,24184,24186,24187,24190,24191,24193,24193,24195,24195,24197,24202,24204,24209,24211,24216,24218,24219,24222,24224,24226,24228,24230,24230,24234,24237,24239,24242,24244,24246,24248,24249,24252,24254,24257,24262,24264,24264,24266,24269,24272,24273,24276,24279,24282,24286,24288,24299,24301,24305,24309,24313,24316,24319,24321,24331,24334,24338,24340,24341,24343,24343,24345,24347,24349,24350,24352,24356,24358,24363,24365,24365,24367,24372,24374,24375,24377,24379,24381,24384,24386,24386,24388,24391,24393,24393,24395,24396,24399,24402,24404,24409,24411,24412,24414,24416,24418,24422,24424,24427,24429,24431,24433,24438,24441,24442,24445,24447,24449,24452,24455,24456,24458,24459,24461,24463,24465,24470,24474,24474,24476,24481,24483,24483,24485,24486,24489,24491,24495,24496,24498,24499,24501,24501,24503,24505,24507,24511,24515,24517,24519,24519,24521,24528,24530,24530,24532,24534,24536,24540,24547,24548,24550,24553,24555,24555,24557,24558,24560,24560,24569,24569,24572,24574,24576,24577,24579,24579,24581,24581,24584,24584,24586,24586,24588,24588,24590,24594,24596,24597,24599,24603,24605,24610,24612,24631,24650,24650,24652,24652,24654,24658,24660,24667,24669,24675,24677,24690,24693,24695,24697,24698,24700,24710,24712,24713,24715,24716,24718,24718,24720,24720,24722,24722,24724,24725,24727,24727,24730,24730,24732,24732,24735,24736,24739,24744,24748,24748,24750,24750,24752,24752,24754,24757,24759,24764,24768,24769,24773,24774,24776,24782,24784,24785,24788,24788,24791,24793,24795,24800,24802,24802,24804,24807,24809,24811,24813,24815,24817,24817,24819,24820,24822,24825,24827,24831,24833,24836,24840,24840,24842,24842,24845,24846,24848,24849,24851,24851,24853,24853,24857,24859,24861,24864,24866,24867,24869,24872,24874,24874,24876,24876,24884,24884,24886,24888,24893,24895,24897,24898,24900,24900,24902,24908,24910,24912,24916,24917,24920,24922,24924,24924,24928,24932,24935,24937,24939,24941,24943,24946,24949,24950,24952,24956,24960,24960,24962,24962,24964,24965,24967,24981,24984,24986,24988,24988,24991,24993,24996,24999,25005,25008,25010,25011,25013,25013,25015,25016,25018,25018,25020,25020,25023,25027,25029,25035,25037,25039,25041,25044,25049,25052,25054,25055,25057,25058,25060,25062,25072,25072,25074,25074,25076,25077,25079,25080,25087,25091,25093,25099,25102,25103,25106,25111,25113,25117,25119,25129,25131,25132,25134,25134,25137,25138,25140,25142,25147,25147,25154,25156,25158,25159,25161,25166,25172,25173,25175,25181,25184,25188,25190,25195,25197,25200,25205,25207,25211,25213,25222,25226,25228,25228,25232,25233,25235,25237,25239,25259,25262,25269,25275,25278,25280,25281,25283,25284,25286,25286,25288,25291,25293,25295,25297,25297,25299,25309,25311,25312,25314,25316,25318,25319,25321,25329,25331,25332,25335,25335,25338,25344,25346,25346,25348,25355,25357,25365,25368,25368,25372,25374,25379,25380,25382,25386,25393,25394,25396,25398,25400,25401,25403,25403,25405,25412,25414,25415,25417,25421,25423,25427,25430,25432,25434,25435,25437,25438,25440,25440,25443,25455,25457,25459,25461,25462,25465,25465,25471,25485,25487,25488,25490,25493,25503,25503,25506,25509,25511,25514,25516,25516,25518,25521,25523,25524,25526,25526,25528,25529,25531,25533,25535,25535,25538,25542,25545,25546,25548,25556,25558,25558,25560,25570,25572,25579,25591,25594,25596,25597,25600,25603,25605,25605,25609,25609,25611,25612,25614,25618,25620,25625,25628,25630,25633,25635,25637,25637,25639,25641,25643,25643,25645,25655,25657,25657,25660,25660,25663,25666,25668,25670,25672,25676,25678,25680,25682,25694,25696,25699,25701,25706,25708,25708,25710,25711,25713,25713,25717,25717,25719,25719,25721,25740,25742,25742,25745,25746,25748,25748,25750,25751,25754,25759,25762,25764,25766,25778,25781,25782,25784,25791,25793,25824,25826,25830,25833,25834,25836,25837,25839,25841,25843,25843,25845,25845,25849,25854,25857,25857,25859,25860,25862,25862,25864,25864,25867,25869,25871,25874,25876,25876,25880,25880,25882,25885,25887,25888,25890,25895,25900,25900,25902,25903,25905,25906,25908,25910,25917,25917,25919,25920,25922,25922,25924,25924,25926,25936,25938,25938,25942,25943,25945,25945,25947,25949,25951,25955,25957,25969,25972,25974,25976,25976,25978,25980,25982,25983,25986,25986,25988,25993,25997,26004,26006,26007,26009,26012,26014,26015,26017,26018,26020,26022,26024,26026,26028,26028,26030,26030,26033,26037,26041,26041,26043,26045,26047,26048,26052,26057,26059,26060,26063,26067,26069,26069,26074,26077,26080,26081,26083,26083,26085,26089,26092,26094,26096,26101,26103,26103,26109,26109,26111,26113,26116,26116,26118,26118,26121,26124,26126,26130,26134,26136,26138,26140,26143,26143,26145,26146,26148,26155,26157,26159,26161,26165,26167,26167,26169,26176,26178,26183,26185,26186,26188,26190,26192,26192,26194,26194,26196,26206,26208,26212,26214,26214,26217,26219,26225,26225,26227,26228,26230,26232,26247,26252,26254,26254,26258,26259,26261,26266,26268,26270,26273,26273,26275,26276,26278,26280,26282,26291,26293,26295,26297,26298,26300,26305,26307,26309,26311,26311,26314,26314,26316,26318,26320,26321,26323,26323,26326,26347,26349,26350,26352,26352,26355,26368,26372,26372,26374,26374,26376,26380,26382,26382,26384,26384,26386,26387,26389,26390,26394,26395,26398,26403,26405,26405,26407,26409,26411,26411,26413,26420,26423,26425,26427,26431,26435,26447,26458,26459,26462,26465,26467,26468,26475,26477,26479,26480,26483,26483,26489,26490,26492,26492,26494,26494,26501,26503,26505,26506,26508,26508,26511,26513,26516,26520,26523,26525,26530,26531,26533,26537,26539,26544,26547,26547,26549,26550,26554,26554,26557,26561,26563,26563,26565,26565,26572,26572,26575,26576,26578,26579,26581,26585,26588,26592,26594,26596,26598,26601,26603,26604,26607,26612,26614,26616,26618,26623,26626,26628,26631,26635,26637,26641,26643,26649,26651,26655,26657,26658,26662,26667,26669,26674,26676,26676,26679,26681,26683,26683,26685,26690,26695,26699,26701,26705,26707,26707,26709,26709,26711,26711,26714,26718,26720,26727,26729,26737,26739,26742,26744,26746,26749,26752,26754,26759,26761,26761,26763,26765,26767,26769,26771,26772,26776,26778,26780,26783,26785,26788,26791,26791,26795,26796,26809,26812,26816,26817,26819,26824,26827,26831,26834,26834,26839,26842,26845,26847,26849,26851,26853,26857,26859,26862,26864,26865,26867,26867,26869,26869,26871,26871,26873,26874,26876,26878,26881,26881,26883,26886,26888,26888,26891,26896,26898,26910,26914,26924,26928,26933,26935,26935,26937,26937,26939,26943,26945,26961,26964,26964,26966,26966,26970,26981,26983,26984,26986,26994,26996,26998,27000,27002,27005,27006,27008,27008,27014,27019,27023,27023,27028,27028,27030,27030,27032,27032,27034,27047,27049,27053,27055,27058,27061,27063,27066,27068,27071,27073,27075,27075,27077,27077,27080,27081,27086,27090,27093,27095,27098,27098,27100,27103,27106,27109,27111,27111,27113,27113,27116,27121,27123,27124,27127,27139,27141,27144,27147,27148,27150,27150,27152,27153,27157,27158,27160,27168,27172,27173,27175,27175,27177,27177,27182,27183,27185,27185,27188,27191,27193,27193,27197,27198,27200,27202,27204,27204,27209,27209,27214,27216,27220,27222,27229,27230,27232,27234,27241,27241,27247,27253,27259,27260,27263,27267,27269,27272,27274,27275,27277,27287,27289,27290,27292,27292,27294,27294,27296,27296,27298,27298,27300,27311,27313,27332,27334,27339,27341,27341,27343,27347,27350,27351,27355,27357,27359,27360,27362,27362,27364,27365,27367,27367,27369,27370,27372,27378,27382,27390,27394,27394,27396,27401,27403,27407,27410,27411,27413,27413,27416,27416,27418,27419,27421,27421,27423,27426,27428,27434,27438,27439,27442,27451,27453,27455,27457,27457,27459,27459,27462,27466,27468,27469,27471,27475,27477,27478,27483,27492,27494,27502,27504,27506,27510,27515,27517,27517,27520,27525,27527,27528,27531,27532,27538,27547,27553,27556,27558,27558,27562,27562,27564,27567,27570,27573,27576,27580,27583,27583,27586,27588,27590,27590,27592,27594,27596,27611,27613,27636,27638,27646,27648,27650,27656,27657,27659,27659,27661,27664,27666,27666,27668,27675,27679,27680,27683,27683,27685,27688,27690,27690,27692,27696,27698,27699,27702,27704,27706,27715,27718,27720,27722,27725,27727,27731,27733,27735,27737,27737,27739,27739,27741,27743,27745,27746,27748,27750,27752,27753,27757,27766,27768,27771,27775,27780,27783,27783,27785,27792,27794,27795,27800,27801,27803,27806,27808,27810,27812,27813,27815,27816,27818,27818,27820,27833,27836,27838,27840,27849,27851,27851,27853,27859,27861,27861,27863,27864,27866,27867,27869,27870,27872,27889,27892,27893,27896,27903,27905,27910,27912,27912,27927,27927,27938,27938,27944,27944,27947,27958,27960,27969,27972,27974,27977,27977,27980,27981,27983,28000,28003,28008,28010,28017,28019,28019,28022,28027,28030,28031,28033,28038,28041,28047,28049,28054,28057,28059,28061,28065,28067,28072,28074,28075,28077,28078,28084,28107,28110,28110,28112,28112,28114,28115,28118,28119,28122,28123,28125,28129,28131,28133,28135,28143,28146,28147,28149,28159,28161,28161,28164,28166,28168,28168,28172,28172,28174,28174,28176,28182,28184,28189,28191,28192,28194,28194,28197,28198,28200,28200,28202,28203,28212,28212,28215,28215,28218,28219,28222,28222,28224,28227,28229,28234,28236,28236,28238,28238,28240,28242,28244,28246,28250,28253,28255,28257,28259,28275,28279,28279,28284,28288,28290,28293,28297,28302,28306,28309,28311,28318,28321,28321,28323,28324,28326,28327,28329,28334,28336,28339,28342,28342,28345,28345,28347,28350,28352,28353,28355,28356,28360,28360,28362,28365,28369,28369,28372,28374,28377,28377,28379,28379,28382,28393,28395,28403,28405,28405,28407,28408,28410,28411,28413,28414,28416,28416,28421,28422,28424,28425,28427,28430,28432,28432,28434,28436,28440,28440,28443,28443,28446,28450,28452,28453,28457,28457,28459,28463,28466,28467,28470,28471,28473,28473,28478,28479,28481,28481,28483,28484,28486,28489,28491,28492,28494,28496,28498,28514,28516,28516,28518,28519,28521,28531,28533,28535,28537,28542,28544,28544,28546,28547,28549,28551,28553,28553,28555,28556,28559,28560,28562,28562,28564,28564,28566,28566,28570,28570,28572,28578,28580,28589,28591,28591,28593,28596,28598,28600,28602,28603,28606,28608,28610,28622,28624,28624,28629,28629,28631,28633,28644,28646,28650,28651,28653,28658,28661,28662,28664,28666,28668,28672,28674,28677,28679,28679,28684,28685,28687,28687,28689,28692,28696,28698,28700,28700,28702,28704,28712,28713,28715,28718,28732,28737,28739,28743,28745,28745,28747,28747,28749,28753,28755,28755,28758,28759,29455,29455,29571,29571,29724,29724,34516,34516,34922,34924,34933,34933,34948,34948,34958,34958'
     

if __name__ == '__main__':
    inserirFaixas()
