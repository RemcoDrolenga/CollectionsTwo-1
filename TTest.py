# def ScoreBoord(Eenen, Tweeën, Drieën, Vieren, Vijfen, Zessen):
#     OpnieuwBlijvenVragen = True
#     while OpnieuwBlijvenVragen == True:
#         WelkeInvullen = input("Welk vakje van het scoreboord wil je invullen? ")
#         WelkeInvullen = WelkeInvullen.lower()
#         if WelkeInvullen == "aces":
#             if Eenen > 0:
#                 VakjeAlIngevuld()
#             else:
#                 Eenen = input("Hoeveel Aces heb je? ")
#                 OpnieuwBlijvenVragen = False
#         elif WelkeInvullen == "twos":
#             if Tweeën > 0:
#                 VakjeAlIngevuld()
#             else:
#                 Tweeën = input("Hoeveel Twos heb je? ")
#                 OpnieuwBlijvenVragen = False
#         elif WelkeInvullen == "threes":
#             if Drieën > 0:
#                 VakjeAlIngevuld()
#             else:
#                 Drieën = input("Hoeveel Threes heb je? ")
#                 OpnieuwBlijvenVragen = False
#         elif  WelkeInvullen == "fours":
#             if Vieren > 0:
#                 VakjeAlIngevuld()
#             else:
#                 Vieren = input("Hoeveel Fours heb je? ")
#                 OpnieuwBlijvenVragen = False
#         elif WelkeInvullen == "fives":
#             if Vijfen > 0:
#                 VakjeAlIngevuld()
#             else:
#                 Vijfen = input("Hoeveel Fives heb je? ")
#                 OpnieuwBlijvenVragen = False
#         elif WelkeInvullen == "sixes":
#             if Zessen > 0:
#                 VakjeAlIngevuld()
#             else:
#                 OpnieuwBlijvenVragen = False
#                 Zessen = input("Hoeveel Sixes heb je? ")
#         print ("Aces ", Eenen)
#         print ("Twos ", Tweeën)
#         print ("Threes ", Drieën)
#         print ("Fours ", Vieren)
#         print ("Fives ", Vijfen)
#         print ("Sixes ", Zessen)
a_dict = {"a":1, "b":2, "c": 3}
values = a_dict. values() 
total = sum(values) 
print(total)