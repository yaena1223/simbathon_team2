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

    # likelion
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

    # elf
    path('elf/',elf,name='elf'),
    path('elf/<str:id>',elf_detail,name='elf_detail'),
    path('elf/new/',elf_new,name='elf_new'),
    path('elf/create/',elf_create,name='elf_create'),
    path('elf/edit/<str:id>',elf_edit,name='elf_edit'),
    path('elf/update/<str:id>',elf_update,name='elf_update'),
    path('elf/delete/<str:id>',elf_delete,name='elf_delete'),
    
    # rcy
    path('rcy/',rcy,name='rcy'),
    path('rcy/<str:id>',rcy_detail,name='rcy_detail'),
    path('rcy/new/',rcy_new,name='rcy_new'),
    path('rcy/create/',rcy_create,name='rcy_create'),
    path('rcy/edit/<str:id>',rcy_edit,name='rcy_edit'),
    path('rcy/update/<str:id>',rcy_update,name='rcy_update'),
    path('rcy/delete/<str:id>',rcy_delete,name='rcy_delete'),

    # road
    path('road/',road,name='road'),
    path('road/<str:id>',road_detail,name='road_detail'),
    path('road/new/',road_new,name='road_new'),
    path('road/create/',road_create,name='road_create'),
    path('road/edit/<str:id>',road_edit,name='road_edit'),
    path('road/update/<str:id>',road_update,name='road_update'),
    path('road/delete/<str:id>',road_delete,name='road_delete'),

    # hand
    path('hand/',hand,name='hand'),
    path('hand/<str:id>',hand_detail,name='hand_detail'),
    path('hand/new/',hand_new,name='hand_new'),
    path('hand/create/',hand_create,name='hand_create'),
    path('hand/edit/<str:id>',hand_edit,name='hand_edit'),
    path('hand/update/<str:id>',hand_update,name='hand_update'),
    path('hand/delete/<str:id>',hand_delete,name='hand_delete'),

    # neighbor
    path('neighbor/',neighbor,name='neighbor'),
    path('neighbor/<str:id>',neighbor_detail,name='neighbor_detail'),
    path('neighbor/new/',neighbor_new,name='neighbor_new'),
    path('neighbor/create/',neighbor_create,name='neighbor_create'),
    path('neighbor/edit/<str:id>',neighbor_edit,name='neighbor_edit'),
    path('neighbor/update/<str:id>',neighbor_update,name='neighbor_update'),
    path('neighbor/delete/<str:id>',neighbor_delete,name='neighbor_delete'),

    # painters
    path('painters/',painters,name='painters'),
    path('painters/<str:id>',painters_detail,name='painters_detail'),
    path('painters/new/',painters_new,name='painters_new'),
    path('painters/create/',painters_create,name='painters_create'),
    path('painters/edit/<str:id>',painters_edit,name='painters_edit'),
    path('painters/update/<str:id>',painters_update,name='painters_update'),
    path('painters/delete/<str:id>',painters_delete,name='painters_delete'),

    # green
    path('green/',green,name='green'),
    path('green/<str:id>',green_detail,name='green_detail'),
    path('green/new/',green_new,name='green_new'),
    path('green/create/',green_create,name='green_create'),
    path('green/edit/<str:id>',green_edit,name='green_edit'),
    path('green/update/<str:id>',green_update,name='green_update'),
    path('green/delete/<str:id>',green_delete,name='green_delete'),

    # korean
    path('korean/',korean,name='korean'),
    path('korean/<str:id>',korean_detail,name='korean_detail'),
    path('korean/new/',korean_new,name='korean_new'),
    path('korean/create/',korean_create,name='korean_create'),
    path('korean/edit/<str:id>',korean_edit,name='korean_edit'),
    path('korean/update/<str:id>',korean_update,name='korean_update'),
    path('korean/delete/<str:id>',korean_delete,name='korean_delete'),

    # draw
    path('draw/',draw,name='draw'),
    path('draw/<str:id>',draw_detail,name='draw_detail'),
    path('draw/new/',draw_new,name='draw_new'),
    path('draw/create/',draw_create,name='draw_create'),
    path('draw/edit/<str:id>',draw_edit,name='draw_edit'),
    path('draw/update/<str:id>',draw_update,name='draw_update'),
    path('draw/delete/<str:id>',draw_delete,name='draw_delete'),

    # literal
    path('literal/',literal,name='literal'),
    path('literal/<str:id>',literal_detail,name='literal_detail'),
    path('literal/new/',literal_new,name='literal_new'),
    path('literal/create/',literal_create,name='literal_create'),
    path('literal/edit/<str:id>',literal_edit,name='literal_edit'),
    path('literal/update/<str:id>',literal_update,name='literal_update'),
    path('literal/delete/<str:id>',literal_delete,name='literal_delete'),

    # calligraphy
    path('calligraphy/',calligraphy,name='calligraphy'),
    path('calligraphy/<str:id>',calligraphy_detail,name='calligraphy_detail'),
    path('calligraphy/new/',calligraphy_new,name='calligraphy_new'),
    path('calligraphy/create/',calligraphy_create,name='calligraphy_create'),
    path('calligraphy/edit/<str:id>',calligraphy_edit,name='calligraphy_edit'),
    path('calligraphy/update/<str:id>',calligraphy_update,name='calligraphy_update'),
    path('calligraphy/delete/<str:id>',calligraphy_delete,name='calligraphy_delete'),

    # circle
    path('circle/',circle,name='circle'),
    path('circle/<str:id>',circle_detail,name='circle_detail'),
    path('circle/new/',circle_new,name='circle_new'),
    path('circle/create/',circle_create,name='circle_create'),
    path('circle/edit/<str:id>',circle_edit,name='circle_edit'),
    path('circle/update/<str:id>',circle_update,name='circle_update'),
    path('circle/delete/<str:id>',circle_delete,name='circle_delete'),

    # stone
    path('stone/',stone,name='stone'),
    path('stone/<str:id>',stone_detail,name='stone_detail'),
    path('stone/new/',stone_new,name='stone_new'),
    path('stone/create/',stone_create,name='stone_create'),
    path('stone/edit/<str:id>',stone_edit,name='stone_edit'),
    path('stone/update/<str:id>',stone_update,name='stone_update'),
    path('stone/delete/<str:id>',stone_delete,name='stone_delete'),

    # cartoon
    path('cartoon/',cartoon,name='cartoon'),
    path('cartoon/<str:id>',cartoon_detail,name='cartoon_detail'),
    path('cartoon/new/',cartoon_new,name='cartoon_new'),
    path('cartoon/create/',cartoon_create,name='cartoon_create'),
    path('cartoon/edit/<str:id>',cartoon_edit,name='cartoon_edit'),
    path('cartoon/update/<str:id>',cartoon_update,name='cartoon_update'),
    path('cartoon/delete/<str:id>',cartoon_delete,name='cartoon_delete'),

    # rush
    path('rush/',rush,name='rush'),
    path('rush/<str:id>',rush_detail,name='rush_detail'),
    path('rush/new/',rush_new,name='rush_new'),
    path('rush/create/',rush_create,name='rush_create'),
    path('rush/edit/<str:id>',rush_edit,name='rush_edit'),
    path('rush/update/<str:id>',rush_update,name='rush_update'),
    path('rush/delete/<str:id>',rush_delete,name='rush_delete'),

    # dust
    path('dust/',dust,name='dust'),
    path('dust/<str:id>',dust_detail,name='dust_detail'),
    path('dust/new/',dust_new,name='dust_new'),
    path('dust/create/',dust_create,name='dust_create'),
    path('dust/edit/<str:id>',dust_edit,name='dust_edit'),
    path('dust/update/<str:id>',dust_update,name='dust_update'),
    path('dust/delete/<str:id>',dust_delete,name='dust_delete'),

    # cave
    path('cave/',cave,name='cave'),
    path('cave/<str:id>',cave_detail,name='cave_detail'),
    path('cave/new/',cave_new,name='cave_new'),
    path('cave/create/',cave_create,name='cave_create'),
    path('cave/edit/<str:id>',cave_edit,name='cave_edit'),
    path('cave/update/<str:id>',cave_update,name='cave_update'),
    path('cave/delete/<str:id>',cave_delete,name='cave_delete'),

    # action
    path('action/',action,name='action'),
    path('action/<str:id>',action_detail,name='action_detail'),
    path('action/new/',action_new,name='action_new'),
    path('action/create/',action_create,name='action_create'),
    path('action/edit/<str:id>',action_edit,name='action_edit'),
    path('action/update/<str:id>',action_update,name='action_update'),
    path('action/delete/<str:id>',action_delete,name='action_delete'),

    # wind
    path('wind/',wind,name='wind'),
    path('wind/<str:id>',wind_detail,name='wind_detail'),
    path('wind/new/',wind_new,name='wind_new'),
    path('wind/create/',wind_create,name='wind_create'),
    path('wind/edit/<str:id>',wind_edit,name='wind_edit'),
    path('wind/update/<str:id>',wind_update,name='wind_update'),
    path('wind/delete/<str:id>',wind_delete,name='wind_delete'),

    # mountain
    path('mountain/',mountain,name='mountain'),
    path('mountain/<str:id>',mountain_detail,name='mountain_detail'),
    path('mountain/new/',mountain_new,name='mountain_new'),
    path('mountain/create/',mountain_create,name='mountain_create'),
    path('mountain/edit/<str:id>',mountain_edit,name='mountain_edit'),
    path('mountain/update/<str:id>',mountain_update,name='mountain_update'),
    path('mountain/delete/<str:id>',mountain_delete,name='mountain_delete'),

    # water
    path('water/',water,name='water'),
    path('water/<str:id>',water_detail,name='water_detail'),
    path('water/new/',water_new,name='water_new'),
    path('water/create/',water_create,name='water_create'),
    path('water/edit/<str:id>',water_edit,name='water_edit'),
    path('water/update/<str:id>',water_update,name='water_update'),
    path('water/delete/<str:id>',water_delete,name='water_delete'),

    # courtist
    path('courtist/',courtist,name='courtist'),
    path('courtist/<str:id>',courtist_detail,name='courtist_detail'),
    path('courtist/new/',courtist_new,name='courtist_new'),
    path('courtist/create/',courtist_create,name='courtist_create'),
    path('courtist/edit/<str:id>',courtist_edit,name='courtist_edit'),
    path('courtist/update/<str:id>',courtist_update,name='courtist_update'),
    path('courtist/delete/<str:id>',courtist_delete,name='courtist_delete'),

    # dutc
    path('dutc/',dutc,name='dutc'),
    path('dutc/<str:id>',dutc_detail,name='dutc_detail'),
    path('dutc/new/',dutc_new,name='dutc_new'),
    path('dutc/create/',dutc_create,name='dutc_create'),
    path('dutc/edit/<str:id>',dutc_edit,name='dutc_edit'),
    path('dutc/update/<str:id>',dutc_update,name='dutc_update'),
    path('dutc/delete/<str:id>',dutc_delete,name='dutc_delete'),


    # fctoto
    path('fctoto/',fctoto,name='fctoto'),
    path('fctoto/<str:id>',fctoto_detail,name='fctoto_detail'),
    path('fctoto/new/',fctoto_new,name='fctoto_new'),
    path('fctoto/create/',fctoto_create,name='fctoto_create'),
    path('fctoto/edit/<str:id>',fctoto_edit,name='fctoto_edit'),
    path('fctoto/update/<str:id>',fctoto_update,name='fctoto_update'),
    path('fctoto/delete/<str:id>',fctoto_delete,name='fctoto_delete'),

    # kendo
    path('kendo/',kendo,name='kendo'),
    path('kendo/<str:id>',kendo_detail,name='kendo_detail'),
    path('kendo/new/',kendo_new,name='kendo_new'),
    path('kendo/create/',kendo_create,name='kendo_create'),
    path('kendo/edit/<str:id>',kendo_edit,name='kendo_edit'),
    path('kendo/update/<str:id>',kendo_update,name='kendo_update'),
    path('kendo/delete/<str:id>',kendo_delete,name='kendo_delete'),

    # lae
    path('lae/',lae,name='lae'),
    path('lae/<str:id>',lae_detail,name='lae_detail'),
    path('lae/new/',lae_new,name='lae_new'),
    path('lae/create/',lae_create,name='lae_create'),
    path('lae/edit/<str:id>',lae_edit,name='lae_edit'),
    path('lae/update/<str:id>',lae_update,name='lae_update'),
    path('lae/delete/<str:id>',lae_delete,name='lae_delete'),

    # baduk
    path('baduk/',baduk,name='baduk'),
    path('baduk/<str:id>',baduk_detail,name='baduk_detail'),
    path('baduk/new/',baduk_new,name='baduk_new'),
    path('baduk/create/',baduk_create,name='baduk_create'),
    path('baduk/edit/<str:id>',baduk_edit,name='baduk_edit'),
    path('baduk/update/<str:id>',baduk_update,name='baduk_update'),
    path('baduk/delete/<str:id>',baduk_delete,name='baduk_delete'),

    # arrow
    path('arrow/',arrow,name='arrow'),
    path('arrow/<str:id>',arrow_detail,name='arrow_detail'),
    path('arrow/new/',arrow_new,name='arrow_new'),
    path('arrow/create/',arrow_create,name='arrow_create'),
    path('arrow/edit/<str:id>',arrow_edit,name='arrow_edit'),
    path('arrow/update/<str:id>',arrow_update,name='arrow_update'),
    path('arrow/delete/<str:id>',arrow_delete,name='arrow_delete'),

    # taekwondo
    path('taekwondo/',taekwondo,name='taekwondo'),
    path('taekwondo/<str:id>',taekwondo_detail,name='taekwondo_detail'),
    path('taekwondo/new/',taekwondo_new,name='taekwondo_new'),
    path('taekwondo/create/',taekwondo_create,name='taekwondo_create'),
    path('taekwondo/edit/<str:id>',taekwondo_edit,name='taekwondo_edit'),
    path('taekwondo/update/<str:id>',taekwondo_update,name='taekwondo_update'),
    path('taekwondo/delete/<str:id>',taekwondo_delete,name='taekwondo_delete'),

    # tuskers
    path('tuskers/',tuskers,name='tuskers'),
    path('tuskers/<str:id>',tuskers_detail,name='tuskers_detail'),
    path('tuskers/new/',tuskers_new,name='tuskers_new'),
    path('tuskers/create/',tuskers_create,name='tuskers_create'),
    path('tuskers/edit/<str:id>',tuskers_edit,name='tuskers_edit'),
    path('tuskers/update/<str:id>',tuskers_update,name='tuskers_update'),
    path('tuskers/delete/<str:id>',tuskers_delete,name='tuskers_delete'),

]