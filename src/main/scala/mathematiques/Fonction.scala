package mathematiques

object Fonction{
    /**
      * 
      * @note Quadratique = z**2+c
      * @param z nombre complexe a testé
      * @param constante constante de la fonction quadratique 
      * @param pressision nombre maximum d'iteration a vérifier
      * @return retourn le nombre d'iteration avant que z ne parte , max pressision
      */
    def quadratique(z : Complexe,constante : Complexe,pressision : Int):Int={
        var  i : Int = 0;
        var  rep : Int = 1;
        var actuel :Complexe =z;
        var distance : Double = constante.im *constante.im +constante.re *constante.re;
        while (distance<4&&rep<=pressision){
            rep+=1;
            actuel=actuel.carre+constante
            i+=1;
            distance=actuel.im*actuel.im+actuel.re*actuel.re
        }
        return i;
    }


}