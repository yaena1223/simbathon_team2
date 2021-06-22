from django.urls import path
from .views import *

app_name="main"
urlpatterns = [
    path('', showmain, name="showmain"),   
    path('faq/',faq,name = 'faq'),
    path('contact/',contact,name='contact'),
    path('academic/', academic, name="academic"),
    path('volunteer/', volunteer, name="volunteer"),
    path('research/', research, name="research"),
    path('art/', art, name="art"),
    path('fresh/', fresh, name="fresh"),
    path('performance/', performance, name="performance"),
    path('atheletic/', atheletic, name="atheletic"),
    path('social/',social,name='social'),

    # 멋사
    path('likelion/',likelion,name='likelion'),
    path('likelion/<str:id>',likelion_detail,name='likelion_detail'),
    path('likelion/new/',likelion_new,name='likelion_new'),
    path('likelion/create/',likelion_create,name='likelion_create'),
    path('likelion/edit/<str:id>',likelion_edit,name='likelion_edit'),
    path('likelion/update/<str:id>',likelion_update,name='likelion_update'),
    path('likelion/delete/<str:id>',likelion_delete,name='likelion_delete'),
   
    # cafein
    path('cafein/',cafein,name='cafein'),
    path('cafein/<str:id>',cafein_detail,name='cafein_detail'),
    path('cafein/new/',cafein_new,name='cafein_new'),
    path('cafein/create/',cafein_create,name='cafein_create'),
    path('cafein/edit/<str:id>',cafein_edit,name='cafein_edit'),
    path('cafein/update/<str:id>',cafein_update,name='cafein_update'),
    path('cafein/delete/<str:id>',cafein_delete,name='cafein_delete'),

    # dna
    path('dna/',dna,name='dna'),
    path('dna/<str:id>',dna_detail,name='dna_detail'),
    path('dna/new/',dna_new,name='dna_new'),
    path('dna/create/',dna_create,name='dna_create'),
    path('dna/edit/<str:id>',dna_edit,name='dna_edit'),
    path('dna/update/<str:id>',dna_update,name='dna_update'),
    path('dna/delete/<str:id>',dna_delete,name='dna_delete'),

    # dussa
    path('dussa/',dussa,name='dussa'),
    path('dussa/<str:id>',dussa_detail,name='dussa_detail'),
    path('dussa/new/',dussa_new,name='dussa_new'),
    path('dussa/create/',dussa_create,name='dussa_create'),
    path('dussa/edit/<str:id>',dussa_edit,name='dussa_edit'),
    path('dussa/update/<str:id>',dussa_update,name='dussa_update'),
    path('dussa/delete/<str:id>',dussa_delete,name='dussa_delete'),

    # kcc
    path('kcc/',kcc,name='kcc'),
    path('kcc/<str:id>',kcc_detail,name='kcc_detail'),
    path('kcc/new/',kcc_new,name='kcc_new'),
    path('kcc/create/',kcc_create,name='kcc_create'),
    path('kcc/edit/<str:id>',kcc_edit,name='kcc_edit'),
    path('kcc/update/<str:id>',kcc_update,name='kcc_update'),
    path('kcc/delete/<str:id>',kcc_delete,name='kcc_delete'),

    # mecs
    path('mecs/',mecs,name='mecs'),
    path('mecs/<str:id>',mecs_detail,name='mecs_detail'),
    path('mecs/new/',mecs_new,name='mecs_new'),
    path('mecs/create/',mecs_create,name='mecs_create'),
    path('mecs/edit/<str:id>',mecs_edit,name='mecs_edit'),
    path('mecs/update/<str:id>',mecs_update,name='mecs_update'),
    path('mecs/delete/<str:id>',mecs_delete,name='mecs_delete'),

    # nsa
    path('nsa/',nsa,name='nsa'),
    path('nsa/<str:id>',nsa_detail,name='nsa_detail'),
    path('nsa/new/',nsa_new,name='nsa_new'),
    path('nsa/create/',nsa_create,name='nsa_create'),
    path('nsa/edit/<str:id>',nsa_edit,name='nsa_edit'),
    path('nsa/update/<str:id>',nsa_update,name='nsa_update'),
    path('nsa/delete/<str:id>',nsa_delete,name='nsa_delete'),

    # marx
    path('marx/',marx,name='marx'),
    path('marx/<str:id>',marx_detail,name='marx_detail'),
    path('marx/new/',marx_new,name='marx_new'),
    path('marx/create/',marx_create,name='marx_create'),
    path('marx/edit/<str:id>',marx_edit,name='marx_edit'),
    path('marx/update/<str:id>',marx_update,name='marx_update'),
    path('marx/delete/<str:id>',marx_delete,name='marx_delete'),

    # management
    path('management/',management,name='management'),
    path('management/<str:id>',management_detail,name='management_detail'),
    path('management/new/',management_new,name='management_new'),
    path('management/create/',management_create,name='management_create'),
    path('management/edit/<str:id>',management_edit,name='management_edit'),
    path('management/update/<str:id>',management_update,name='management_update'),
    path('management/delete/<str:id>',management_delete,name='management_delete'),

    # economy
    path('economy/',economy,name='economy'),
    path('economy/<str:id>',economy_detail,name='economy_detail'),
    path('economy/new/',economy_new,name='economy_new'),
    path('economy/create/',economy_create,name='economy_create'),
    path('economy/edit/<str:id>',economy_edit,name='economy_edit'),
    path('economy/update/<str:id>',economy_update,name='economy_update'),
    path('economy/delete/<str:id>',economy_delete,name='economy_delete'),

    # international
    path('international/',international,name='international'),
    path('international/<str:id>',international_detail,name='international_detail'),
    path('international/new/',international_new,name='international_new'),
    path('international/create/',international_create,name='international_create'),
    path('international/edit/<str:id>',international_edit,name='international_edit'),
    path('international/update/<str:id>',international_update,name='international_update'),
    path('international/delete/<str:id>',international_delete,name='international_delete'),

    # politics
    path('politics/',politics,name='politics'),
    path('politics/<str:id>',politics_detail,name='politics_detail'),
    path('politics/new/',politics_new,name='politics_new'),
    path('politics/create/',politics_create,name='politics_create'),
    path('politics/edit/<str:id>',politics_edit,name='politics_edit'),
    path('politics/update/<str:id>',politics_update,name='politics_update'),
    path('politics/delete/<str:id>',politics_delete,name='politics_delete'),

    path('elf/',elf,name='elf'),
    path('rcy/',rcy,name='rcy'),
    path('road/',road,name='road'),
    path('hand/',hand,name='hand'),
    path('neighbor/',neighbor,name='neighbor'),
    path('painters/',painters,name='painters'),
    path('green/',green,name='green'),
    path('korean/',korean,name='korean'),

    # kusa
    path('kusa/',kusa,name='kusa'),
    path('kusa/<str:id>',kusa_detail,name='kusa_detail'),
    path('kusa/new/',kusa_new,name='kusa_new'),
    path('kusa/create/',kusa_create,name='kusa_create'),
    path('kusa/edit/<str:id>',kusa_edit,name='kusa_edit'),
    path('kusa/update/<str:id>',kusa_update,name='kusa_update'),
    path('kusa/delete/<str:id>',kusa_delete,name='kusa_delete'),

    # rich
    path('rich/',rich,name='rich'),
    path('rich/<str:id>',rich_detail,name='rich_detail'),
    path('rich/new/',rich_new,name='rich_new'),
    path('rich/create/',rich_create,name='rich_create'),
    path('rich/edit/<str:id>',rich_edit,name='rich_edit'),
    path('rich/update/<str:id>',rich_update,name='rich_update'),
    path('rich/delete/<str:id>',rich_delete,name='rich_delete'),

    # unsa
    path('unsa/',unsa,name='unsa'),
    path('unsa/<str:id>',unsa_detail,name='unsa_detail'),
    path('unsa/new/',unsa_new,name='unsa_new'),
    path('unsa/create/',unsa_create,name='unsa_create'),
    path('unsa/edit/<str:id>',unsa_edit,name='unsa_edit'),
    path('unsa/update/<str:id>',unsa_update,name='unsa_update'),
    path('unsa/delete/<str:id>',unsa_delete,name='unsa_delete'),

    # frontier
    path('froniter/',frontier,name='frontier'),
    path('frontier/<str:id>',frontier_detail,name='frontier_detail'),
    path('frontier/new/',frontier_new,name='frontier_new'),
    path('frontier/create/',frontier_create,name='frontier_create'),
    path('frontier/edit/<str:id>',frontier_edit,name='frontier_edit'),
    path('frontier/update/<str:id>',frontier_update,name='frontier_update'),
    path('frontier/delete/<str:id>',frontier_delete,name='frontier_delete'),

    # buddha
    path('buddha/',buddha,name='buddha'),
    path('buddha/<str:id>',buddha_detail,name='buddha_detail'),
    path('buddha/new/',buddha_new,name='buddha_new'),
    path('buddha/create/',buddha_create,name='buddha_create'),
    path('buddha/edit/<str:id>',buddha_edit,name='buddha_edit'),
    path('buddha/update/<str:id>',buddha_update,name='buddha_update'),
    path('buddha/delete/<str:id>',buddha_delete,name='buddha_delete'),

    path('dust/',dust,name='dust'),
    path('cave/',cave,name='cave'),
    path('action/',action,name='action'),
    path('wind/',wind,name='wind'),
    path('mountatin/',mountain,name='mountain'),
    path('water/',water,name='water'),
    path('courtist/',courtist,name='courtist'),
    path('dutc/',dutc,name='dutc'),
    path('fctoto/',fctoto,name='fctoto'),
    path('lae/',lae,name='lae'),
    path('kendo/',kendo,name='kendo'),
    path('baduk/',baduk,name='baduk'),
    path('arrow/',dust,name='arrow'),
    path('taekwondo/',taekwondo,name='taekwondo'),
    path('tuskers/',tuskers,name='tuskers'),

    #ajax
    path('ajax/',ajax,name='ajax'),
    path('ajax/<str:id>',ajax_detail,name='ajax_detail'),
    path('ajax/new/',ajax_new,name='ajax_new'),
    path('ajax/create/',ajax_create,name='ajax_create'),
    path('ajax/edit/<str:id>',ajax_edit,name='ajax_edit'),
    path('ajax/update/<str:id>',ajax_update,name='ajax_update'),
    path('ajax/delete/<str:id>',ajax_delete,name='ajax_delete'),


    #hola
    path('hola/',hola,name='hola'),
    path('hola/<str:id>',hola_detail,name='hola_detail'),
    path('hola/new/',hola_new,name='hola_new'),
    path('hola/create/',hola_create,name='hola_create'),
    path('hola/edit/<str:id>',hola_edit,name='hola_edit'),
    path('hola/update/<str:id>',hola_update,name='hola_update'),
    path('hola/delete/<str:id>',hola_delete,name='hola_delete'),

    #odc
    path('odc/',odc,name='odc'),
    path('odc/<str:id>',odc_detail,name='odc_detail'),
    path('odc/new/',odc_new,name='odc_new'),
    path('odc/create/',odc_create,name='odc_create'),
    path('odc/edit/<str:id>',odc_edit,name='odc_edit'),
    path('odc/update/<str:id>',odc_update,name='odc_update'),
    path('odc/delete/<str:id>',odc_delete,name='odc_delete'),

    #opus
    path('opus/',opus,name='opus'),
    path('opus/<str:id>',opus_detail,name='opus_detail'),
    path('opus/new/',opus_new,name='opus_new'),
    path('opus/create/',opus_create,name='opus_create'),
    path('opus/edit/<str:id>',opus_edit,name='opus_edit'),
    path('opus/update/<str:id>',opus_update,name='opus_update'),
    path('opus/delete/<str:id>',opus_delete,name='opus_delete'),

    #drama
    path('drama/',drama,name='drama'),
    path('drama/<str:id>',drama_detail,name='drama_detail'),
    path('drama/new/',drama_new,name='drama_new'),
    path('drama/create/',drama_create,name='drama_create'),
    path('drama/edit/<str:id>',drama_edit,name='drama_edit'),
    path('drama/update/<str:id>',drama_update,name='drama_update'),
    path('drama/delete/<str:id>',drama_delete,name='drama_delete'),

    #lotus
    path('lotus/',lotus,name='lotus'),
    path('lotus/<str:id>',lotus_detail,name='lotus_detail'),
    path('lotus/new/',lotus_new,name='lotus_new'),
    path('lotus/create/',lotus_create,name='lotus_create'),
    path('lotus/edit/<str:id>',lotus_edit,name='lotus_edit'),
    path('lotus/update/<str:id>',lotus_update,name='lotus_update'),
    path('lotus/delete/<str:id>',lotus_delete,name='lotus_delete'),

    #cloud
    path('cloud/',cloud,name='cloud'),
    path('cloud/<str:id>',cloud_detail,name='cloud_detail'),
    path('cloud/new/',cloud_new,name='cloud_new'),
    path('cloud/create/',cloud_create,name='cloud_create'),
    path('cloud/edit/<str:id>',cloud_edit,name='cloud_edit'),
    path('cloud/update/<str:id>',cloud_update,name='cloud_update'),
    path('cloud/delete/<str:id>',cloud_delete,name='cloud_delete'),

    #arirang
    path('arirang/',arirang,name='arirang'),
    path('arirang/<str:id>',arirang_detail,name='arirang_detail'),
    path('arirang/new/',arirang_new,name='arirang_new'),
    path('arirang/create/',arirang_create,name='arirang_create'),
    path('arirang/edit/<str:id>',arirang_edit,name='arirang_edit'),
    path('arirang/update/<str:id>',arirang_update,name='arirang_update'),
    path('arirang/delete/<str:id>',arirang_delete,name='arirang_delete'),

    #eumsem
    path('eumsem/',eumsem,name='eumsem'),
    path('eumsem/<str:id>',eumsem_detail,name='eumsem_detail'),
    path('eumsem/new/',eumsem_new,name='eumsem_new'),
    path('eumsem/create/',eumsem_create,name='eumsem_create'),
    path('eumsem/edit/<str:id>',eumsem_edit,name='eumsem_edit'),
    path('eumsem/update/<str:id>',eumsem_update,name='eumsem_update'),
    path('eumsem/delete/<str:id>',eumsem_delete,name='eumsem_delete'),

    #fearless
    path('fearless/',fearless,name='fearless'),
    path('fearless/<str:id>',fearless_detail,name='fearless_detail'),
    path('fearless/new/',fearless_new,name='fearless_new'),
    path('fearless/create/',fearless_create,name='fearless_create'),
    path('fearless/edit/<str:id>',fearless_edit,name='fearless_edit'),
    path('fearless/update/<str:id>',fearless_update,name='fearless_update'),
    path('fearless/delete/<str:id>',fearless_delete,name='fearless_delete'),

    #yeoul
    path('yeoul/',yeoul,name='yeoul'),
    path('yeoul/<str:id>',yeoul_detail,name='yeoul_detail'),
    path('yeoul/new/',yeoul_new,name='yeoul_new'),
    path('yeoul/create/',yeoul_create,name='yeoul_create'),
    path('yeoul/edit/<str:id>',yeoul_edit,name='yeoul_edit'),
    path('yeoul/update/<str:id>',yeoul_update,name='yeoul_update'),
    path('yeoul/delete/<str:id>',yeoul_delete,name='yeoul_delete'),

    path('draw/',draw,name='draw'),
    path('literal/',literal,name='literal'),
    path('calligraphy/',calligraphy,name='calligraphy'),
    path('circle/',circle,name='circle'),
    path('stone/',stone,name='stone'),
    path('cartoon/',cartoon,name='cartoon'),
    path('rush/',rush,name='rush'),

    # elephente
    path('elephente/',elephente,name='elephente'),
    path('elephente/<str:id>',elephente_detail,name='elephente_detail'),
    path('elephente/new/',elephente_new,name='elephente_new'),
    path('elephente/create/',elephente_create,name='elephente_create'),
    path('elephente/edit/<str:id>',elephente_edit,name='elephente_edit'),
    path('elephente/update/<str:id>',elephente_update,name='elephente_update'),
    path('elephente/delete/<str:id>',elephente_delete,name='elephente_delete'),

    # doomchit
    path('doomchit/',doomchit,name='doomchit'),
    path('doomchit/<str:id>',doomchit_detail,name='doomchit_detail'),
    path('doomchit/new/',doomchit_new,name='doomchit_new'),
    path('doomchit/create/',doomchit_create,name='doomchit_create'),
    path('doomchit/edit/<str:id>',doomchit_edit,name='doomchit_edit'),
    path('doomchit/update/<str:id>',doomchit_update,name='doomchit_update'),
    path('doomchit/delete/<str:id>',doomchit_delete,name='doomchit_delete'),

    # enactus
    path('enactus/',enactus,name='enactus'),
    path('enactus/<str:id>',enactus_detail,name='enactus_detail'),
    path('enactus/new/',enactus_new,name='enactus_new'),
    path('enactus/create/',enactus_create,name='enactus_create'),
    path('enactus/edit/<str:id>',enactus_edit,name='enactus_edit'),
    path('enactus/update/<str:id>',enactus_update,name='enactus_update'),
    path('enactus/delete/<str:id>',enactus_delete,name='enactus_delete'),

    # jam
    path('jam/',jam,name='jam'),
    path('jam/<str:id>',jam_detail,name='jam_detail'),
    path('jam/new/',jam_new,name='jam_new'),
    path('jam/create/',jam_create,name='jam_create'),
    path('jam/edit/<str:id>',jam_edit,name='jam_edit'),
    path('jam/update/<str:id>',jam_update,name='jam_update'),
    path('jam/delete/<str:id>',jam_delete,name='jam_delete'),
    
    # qud
    path('qud/',qud,name='qud'),
    path('qud/<str:id>',qud_detail,name='qud_detail'),
    path('qud/new/',qud_new,name='qud_new'),
    path('qud/create/',qud_create,name='qud_create'),
    path('qud/edit/<str:id>',qud_edit,name='qud_edit'),
    path('qud/update/<str:id>',qud_update,name='qud_update'),
    path('qud/delete/<str:id>',qud_delete,name='qud_delete'),

]