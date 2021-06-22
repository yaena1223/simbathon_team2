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

    path('dna/',dna,name='dna'),
    path('dussa/',dussa,name='dussa'),
    path('kcc/',kcc,name='kcc'),
    path('mecs/',mecs,name='mecs'),
    path('nsa/',nsa,name='nsa'),
    path('marx/',marx,name='marx'),

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

    path('kusa/',kusa,name='kusa'),
    path('rich/',rich,name='rich'),
    path('unsa/',unsa,name='unsa'),
    path('froniter/',frontier,name='frontier'),
    path('buddha/',buddha,name='buddha'),

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

    path('elephente/',elephente,name='elephente'),
    path('doomchit/',doomchit,name='doomchit'),
    path('enactus/',enactus,name='enactus'),
    path('jam/',jam,name='jam'),
    path('qud/',qud,name='qud'),

]