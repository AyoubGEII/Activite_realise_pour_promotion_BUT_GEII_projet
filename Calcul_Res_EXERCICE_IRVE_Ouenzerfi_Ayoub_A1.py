Score_previous = 10 #Valeur de départ
SerieE12 = [100,120,150,180,220,330,390,470,560,680,820] #La série E12 sur 2 décades afin d'avoir un rapport différents
V_low = 3.3   #La tension voulu maximal en sorti


for R3 in SerieE12: 
    for R2 in SerieE12 :
        for R1 in SerieE12 : #Rentre dans les 3 for afin de vérifier 
            Cp_high = ((12/R1)+(V_low/R3))/((1/R1)+(1/R2)+(1/R3))  #Equation du théoreme de millman pour 5v à partir de 12v
            Cp_low = (-12/R1)+(V_low/R3)     #Equation th millman pour 0v à partir du -12v définie au tableau + photo
            if (0 <= Cp_low) and (Cp_high<= V_low) :    #Test que nos valeurs son comprise dans l'intervalle voulu
                Score = (Cp_low - 0) + (V_low-Cp_high)  #Permet de connaître notre écart
                if Score<Score_previous :
                    Score_previous=Score                #L'écart égale la valeur d'avant donc il tourne jusqu'a avoir la plus petit valeur d'écart possible avec nos combinaison
                    print("------")
                    print("R3 = " + str(R3))
                    print("R2 = " + str(R2))
                    print("R1 = " + str(R1))
                    print("Valeur de proche de 5 V =" + str(Cp_high))
                    print("Valeur de proche de 0 V =" + str(Cp_low))
                    print("//////")
                    print("Affichage du score le plus bas : ")
                    print(Score,"≈ 0")
                    print("//////")
                    print("--------")
                    #Ce programme remplace un tableau excel avec toutes les disponibilitées soit 22*22*22 = 10648 tests possibles pour nos valeurs
