bigchars = [
"               AAA               BBBBBBBBBBBBBBBBB           CCCCCCCCCCCCCDDDDDDDDDDDDD        EEEEEEEEEEEEEEEEEEEEEEFFFFFFFFFFFFFFFFFFFFFF        GGGGGGGGGGGGGHHHHHHHHH     HHHHHHHHHIIIIIIIIII          JJJJJJJJJJJKKKKKKKKK    KKKKKKKLLLLLLLLLLL             MMMMMMMM               MMMMMMMMNNNNNNNN        NNNNNNNN     OOOOOOOOO     PPPPPPPPPPPPPPPPP        QQQQQQQQQ     RRRRRRRRRRRRRRRRR      SSSSSSSSSSSSSSS TTTTTTTTTTTTTTTTTTTTTTTUUUUUUUU     UUUUUUUUVVVVVVVV           VVVVVVVVWWWWWWWW                           WWWWWWWWXXXXXXX       XXXXXXXYYYYYYY       YYYYYYYZZZZZZZZZZZZZZZZZZZ     000000000       1111111    222222222222222     333333333333333          444444444  555555555555555555         66666666   77777777777777777777     888888888          999999999     ",
"              A:::A              B::::::::::::::::B       CCC::::::::::::CD::::::::::::DDD     E::::::::::::::::::::EF::::::::::::::::::::F     GGG::::::::::::GH:::::::H     H:::::::HI::::::::I          J:::::::::JK:::::::K    K:::::KL:::::::::L             M:::::::M             M:::::::MN:::::::N       N::::::N   OO:::::::::OO   P::::::::::::::::P     QQ:::::::::QQ   R::::::::::::::::R   SS:::::::::::::::ST:::::::::::::::::::::TU::::::U     U::::::UV::::::V           V::::::VW::::::W                           W::::::WX:::::X       X:::::XY:::::Y       Y:::::YZ:::::::::::::::::Z   00:::::::::00    1::::::1   2:::::::::::::::22  3:::::::::::::::33       4::::::::4  5::::::::::::::::5        6::::::6    7::::::::::::::::::7   88:::::::::88      99:::::::::99   ",
"             A:::::A             B::::::BBBBBB:::::B    CC:::::::::::::::CD:::::::::::::::DD   E::::::::::::::::::::EF::::::::::::::::::::F   GG:::::::::::::::GH:::::::H     H:::::::HI::::::::I          J:::::::::JK:::::::K    K:::::KL:::::::::L             M::::::::M           M::::::::MN::::::::N      N::::::N OO:::::::::::::OO P::::::PPPPPP:::::P  QQ:::::::::::::QQ R::::::RRRRRR:::::R S:::::SSSSSS::::::ST:::::::::::::::::::::TU::::::U     U::::::UV::::::V           V::::::VW::::::W                           W::::::WX:::::X       X:::::XY:::::Y       Y:::::YZ:::::::::::::::::Z 00:::::::::::::00 1:::::::1   2::::::222222:::::2 3::::::33333::::::3     4:::::::::4  5::::::::::::::::5       6::::::6     7::::::::::::::::::7 88:::::::::::::88  99:::::::::::::99 ",
"            A:::::::A            BB:::::B     B:::::B  C:::::CCCCCCCC::::CDDD:::::DDDDD:::::D  EE::::::EEEEEEEEE::::EFF::::::FFFFFFFFF::::F  G:::::GGGGGGGG::::GHH::::::H     H::::::HHII::::::II          JJ:::::::JJK:::::::K   K::::::KLL:::::::LL             M:::::::::M         M:::::::::MN:::::::::N     N::::::NO:::::::OOO:::::::OPP:::::P     P:::::PQ:::::::QQQ:::::::QRR:::::R     R:::::RS:::::S     SSSSSSST:::::TT:::::::TT:::::TUU:::::U     U:::::UUV::::::V           V::::::VW::::::W                           W::::::WX::::::X     X::::::XY::::::Y     Y::::::YZ:::ZZZZZZZZ:::::Z 0:::::::000:::::::0111:::::1   2222222     2:::::2 3333333     3:::::3    4::::44::::4  5:::::555555555555      6::::::6      777777777777:::::::78::::::88888::::::89::::::99999::::::9",
"           A:::::::::A             B::::B     B:::::B C:::::C       CCCCCC  D:::::D    D:::::D   E:::::E       EEEEEE  F:::::F       FFFFFF G:::::G       GGGGGG  H:::::H     H:::::H    I::::I              J:::::J  KK::::::K  K:::::KKK  L:::::L               M::::::::::M       M::::::::::MN::::::::::N    N::::::NO::::::O   O::::::O  P::::P     P:::::PQ::::::Q   Q::::::Q  R::::R     R:::::RS:::::S            TTTTTT  T:::::T  TTTTTT U:::::U     U:::::U  V:::::V           V:::::V  W:::::W           WWWWW           W:::::W XXX:::::X   X:::::XXXYYY:::::Y   Y:::::YYYZZZZZ     Z:::::Z  0::::::0   0::::::0   1::::1               2:::::2             3:::::3   4::::4 4::::4  5:::::5                6::::::6                  7::::::7 8:::::8     8:::::89:::::9     9:::::9",
"          A:::::A:::::A            B::::B     B:::::BC:::::C                D:::::D     D:::::D  E:::::E               F:::::F             G:::::G                H:::::H     H:::::H    I::::I              J:::::J    K:::::K K:::::K     L:::::L               M:::::::::::M     M:::::::::::MN:::::::::::N   N::::::NO:::::O     O:::::O  P::::P     P:::::PQ:::::Q     Q:::::Q  R::::R     R:::::RS:::::S                    T:::::T         U:::::U     U:::::U   V:::::V         V:::::V    W:::::W         W:::::W         W:::::W     X:::::X X:::::X      Y:::::Y Y:::::Y           Z:::::Z    0:::::0     0:::::0   1::::1               2:::::2             3:::::3  4::::4  4::::4  5:::::5               6::::::6                  7::::::7  8:::::8     8:::::89:::::9     9:::::9",
"         A:::::A A:::::A           B::::BBBBBB:::::B C:::::C                D:::::D     D:::::D  E::::::EEEEEEEEEE     F::::::FFFFFFFFFF   G:::::G                H::::::HHHHH::::::H    I::::I              J:::::J    K::::::K:::::K      L:::::L               M:::::::M::::M   M::::M:::::::MN:::::::N::::N  N::::::NO:::::O     O:::::O  P::::PPPPPP:::::P Q:::::Q     Q:::::Q  R::::RRRRRR:::::R  S::::SSSS                 T:::::T         U:::::U     U:::::U    V:::::V       V:::::V      W:::::W       W:::::::W       W:::::W       X:::::X:::::X        Y:::::Y:::::Y           Z:::::Z     0:::::0     0:::::0   1::::1            2222::::2      33333333:::::3  4::::4   4::::4  5:::::5555555555     6::::::6                  7::::::7    8:::::88888:::::8  9:::::99999::::::9",
"        A:::::A   A:::::A          B:::::::::::::BB  C:::::C                D:::::D     D:::::D  E:::::::::::::::E     F:::::::::::::::F   G:::::G    GGGGGGGGGG  H:::::::::::::::::H    I::::I              J:::::j    K:::::::::::K       L:::::L               M::::::M M::::M M::::M M::::::MN::::::N N::::N N::::::NO:::::O     O:::::O  P:::::::::::::PP  Q:::::Q     Q:::::Q  R:::::::::::::RR    SS::::::SSSSS            T:::::T         U:::::U     U:::::U     V:::::V     V:::::V        W:::::W     W:::::::::W     W:::::W         X:::::::::X          Y:::::::::Y           Z:::::Z      0:::::0 000 0:::::0   1::::l       22222::::::22       3:::::::::::3  4::::444444::::4445:::::::::::::::5   6::::::::66666            7::::::7      8:::::::::::::8    99::::::::::::::9",
"       A:::::A     A:::::A         B::::BBBBBB:::::B C:::::C                D:::::D     D:::::D  E:::::::::::::::E     F:::::::::::::::F   G:::::G    G::::::::G  H:::::::::::::::::H    I::::I              J:::::J    K:::::::::::K       L:::::L               M::::::M  M::::M::::M  M::::::MN::::::N  N::::N:::::::NO:::::O     O:::::O  P::::PPPPPPPPP    Q:::::Q     Q:::::Q  R::::RRRRRR:::::R     SSS::::::::SS          T:::::T         U:::::U     U:::::U      V:::::V   V:::::V          W:::::W   W:::::W:::::W   W:::::W          X:::::::::X           Y:::::::Y           Z:::::Z       0:::::0 000 0:::::0   1::::l     22::::::::222         33333333:::::3 4::::::::::::::::4555555555555:::::5 6::::::::::::::66         7::::::7      8:::::88888:::::8     99999::::::::9 ",
"      A:::::AAAAAAAAA:::::A        B::::B     B:::::BC:::::C                D:::::D     D:::::D  E::::::EEEEEEEEEE     F::::::FFFFFFFFFF   G:::::G    GGGGG::::G  H::::::HHHHH::::::H    I::::I  JJJJJJJ     J:::::J    K::::::K:::::K      L:::::L               M::::::M   M:::::::M   M::::::MN::::::N   N:::::::::::NO:::::O     O:::::O  P::::P            Q:::::Q     Q:::::Q  R::::R     R:::::R       SSSSSS::::S         T:::::T         U:::::U     U:::::U       V:::::V V:::::V            W:::::W W:::::W W:::::W W:::::W          X:::::X:::::X           Y:::::Y           Z:::::Z        0:::::0     0:::::0   1::::l    2:::::22222                    3:::::34444444444:::::444            5:::::56::::::66666:::::6       7::::::7      8:::::8     8:::::8         9::::::9  ",
"     A:::::::::::::::::::::A       B::::B     B:::::BC:::::C                D:::::D     D:::::D  E:::::E               F:::::F             G:::::G        G::::G  H:::::H     H:::::H    I::::I  J:::::J     J:::::J    K:::::K K:::::K     L:::::L               M::::::M    M:::::M    M::::::MN::::::N    N::::::::::NO:::::O     O:::::O  P::::P            Q:::::Q  QQQQ:::::Q  R::::R     R:::::R            S:::::S        T:::::T         U:::::U     U:::::U        V:::::V:::::V              W:::::W:::::W   W:::::W:::::W          X:::::X X:::::X          Y:::::Y          Z:::::Z         0:::::0     0:::::0   1::::l   2:::::2                         3:::::3          4::::4              5:::::56:::::6     6:::::6     7::::::7       8:::::8     8:::::8        9::::::9   ",
"    A:::::AAAAAAAAAAAAA:::::A      B::::B     B:::::B C:::::C       CCCCCC  D:::::D    D:::::D   E:::::E       EEEEEE  F:::::F              G:::::G       G::::G  H:::::H     H:::::H    I::::I  J::::::J   J::::::J  KK::::::K  K:::::KKK  L:::::L         LLLLLLM::::::M     MMMMM     M::::::MN::::::N     N:::::::::NO::::::O   O::::::O  P::::P            Q::::::Q Q::::::::Q  R::::R     R:::::R            S:::::S        T:::::T         U::::::U   U::::::U         V:::::::::V                W:::::::::W     W:::::::::W        XXX:::::X   X:::::XXX       Y:::::Y       ZZZ:::::Z     ZZZZZ0::::::0   0::::::0   1::::l   2:::::2                         3:::::3          4::::4  5555555     5:::::56:::::6     6:::::6    7::::::7        8:::::8     8:::::8       9::::::9    ",
"   A:::::A             A:::::A   BB:::::BBBBBB::::::B  C:::::CCCCCCCC::::CDDD:::::DDDDD:::::D  EE::::::EEEEEEEE:::::EFF:::::::FF             G:::::GGGGGGGG::::GHH::::::H     H::::::HHII::::::IIJ:::::::JJJ:::::::J  K:::::::K   K::::::KLL:::::::LLLLLLLLL:::::LM::::::M               M::::::MN::::::N      N::::::::NO:::::::OOO:::::::OPP::::::PP          Q:::::::QQ::::::::QRR:::::R     R:::::RSSSSSSS     S:::::S      TT:::::::TT       U:::::::UUU:::::::U          V:::::::V                  W:::::::W       W:::::::W         X::::::X     X::::::X       Y:::::Y       Z::::::ZZZZZZZZ:::Z0:::::::000:::::::0111::::::1112:::::2       2222223333333     3:::::3          4::::4  5::::::55555::::::56::::::66666::::::6   7::::::7         8::::::88888::::::8      9::::::9     ",
"  A:::::A               A:::::A  B:::::::::::::::::B    CC:::::::::::::::CD:::::::::::::::DD   E::::::::::::::::::::EF::::::::FF              GG:::::::::::::::GH:::::::H     H:::::::HI::::::::I JJ:::::::::::::JJ   K:::::::K    K:::::KL::::::::::::::::::::::LM::::::M               M::::::MN::::::N       N:::::::N OO:::::::::::::OO P::::::::P           QQ::::::::::::::Q R::::::R     R:::::RS::::::SSSSSS:::::S      T:::::::::T        UU:::::::::::::UU            V:::::V                    W:::::W         W:::::W          X:::::X       X:::::X    YYYY:::::YYYY    Z:::::::::::::::::Z 00:::::::::::::00 1::::::::::12::::::2222222:::::23::::::33333::::::3        44::::::44 55:::::::::::::55  66:::::::::::::66   7::::::7           88:::::::::::::88      9::::::9      ",
" A:::::A                 A:::::A B::::::::::::::::B       CCC::::::::::::CD::::::::::::DDD     E::::::::::::::::::::EF::::::::FF                GGG::::::GGG:::GH:::::::H     H:::::::HI::::::::I   JJ:::::::::JJ     K:::::::K    K:::::KL::::::::::::::::::::::LM::::::M               M::::::MN::::::N        N::::::N   OO:::::::::OO   P::::::::P             QQ:::::::::::Q  R::::::R     R:::::RS:::::::::::::::SS       T:::::::::T          UU:::::::::UU               V:::V                      W:::W           W:::W           X:::::X       X:::::X    Y:::::::::::Y    Z:::::::::::::::::Z   00:::::::::00   1::::::::::12::::::::::::::::::23:::::::::::::::33         4::::::::4   55:::::::::55      66:::::::::66    7::::::7              88:::::::::88       9::::::9       ",
"AAAAAAA                   AAAAAAABBBBBBBBBBBBBBBBB           CCCCCCCCCCCCCDDDDDDDDDDDDD        EEEEEEEEEEEEEEEEEEEEEEFFFFFFFFFFF                   GGGGGG   GGGGHHHHHHHHH     HHHHHHHHHIIIIIIIIII     JJJJJJJJJ       KKKKKKKKK    KKKKKKKLLLLLLLLLLLLLLLLLLLLLLLLMMMMMMMM               MMMMMMMMNNNNNNNN         NNNNNNN     OOOOOOOOO     PPPPPPPPPP               QQQQQQQQ::::QQRRRRRRRR     RRRRRRR SSSSSSSSSSSSSSS         TTTTTTTTTTT            UUUUUUUUU                  VVV                        WWW             WWW            XXXXXXX       XXXXXXX    YYYYYYYYYYYYY    ZZZZZZZZZZZZZZZZZZZ     000000000     11111111111122222222222222222222 333333333333333           4444444444     555555555          666666666     77777777                 888888888        99999999        "
]

nome = input("Insira o nome que deseja imprimir: ").upper() #Aqui vamos inserir o nome que queremos exibir em letras grandes;
inicio = {} #Aqui será onde a posição de inicio de cada letra será guardada no dicionario;
fim = {} #Aqui será onde será guardada a posição final de cada letra;
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" #Lista com todos os caracteres que podemos exibir em letras grandes;

for letra in alfabeto:
    inicio_letra = bigchars[0].find(letra) #Aqui vamos acha a primeira posição onde cada letra da lista alfabeto pode ser encontrada;
    fim_letra = bigchars[0].rfind(letra) #Aqui vamos achar a ultima posição de cada letra que podemos encontrar na nossa lista;
    for l in bigchars: #Aqui vamos comparar cada incidencia da letra e decidir onde podemos dizer que realmente é o começo de cada letra;
        if l.find(letra) < inicio_letra: #Comparamos a ultima posição que temos com a nova posição que achamos, sucessivamente;
            inicio_letra = l.find(letra)
        if l.rfind(letra) > fim_letra: #Comparamos a ultima posição que temos com a nova posição que achamos, sucessivamente;
            fim_letra = l.rfind(letra)
    inicio[letra] = inicio_letra #No final quando achamos a menor primeira posição e a maior ultima posição, guardamos esses dados no dicionario;
    fim[letra] = fim_letra #Fiz um dicionario para a posição final e inicial;

for l in bigchars:
    for letra in nome: #No final vamos imprimir a primeira posição e a ultima posição da letra, percorrendo a lista bigchars;
        print(l[inicio[letra]:fim[letra]+1], end="")
    print() #Ao final de cada termo de bigchars, temos que pular uma linha para que o que é exibido possa ser compreendido;
    