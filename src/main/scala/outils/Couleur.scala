package outils
import java.awt.Color

object Couleur{
    /**
      * 
      *
      * @param valeur entier entre 0 - maximum 
      * @param maximum entier maximum
      * @return Couleur en niveau de gris
      */
    def Gris(valeur:Int, maximum :Int):Color={
        var v : Float = valeur;
        if(valeur<0) v=0;
        else if(valeur>maximum)v=maximum;
        val niveau : Float = v/maximum;
        return new Color(niveau,niveau,niveau);
    }
    /**
      * 
      *
      * @param longeur_Onde entier entre 0 - 270
      * @return
      */
    def Onde(longeur_Onde: Int): Color = {
        if(longeur_Onde<0||longeur_Onde>270) new Color(0,0,0);
        if (longeur_Onde < 60 ) {
            new Color(((-longeur_Onde + 60) / (60 - 0) * 255).toInt, 0, 255)
        } else if (longeur_Onde < 110) {
            new Color(0, ((longeur_Onde - 60) / (110 - 60) * 255).toInt, 255)
        } else if (longeur_Onde < 130) {
            new Color(0, 255, (-(longeur_Onde - 130) / (130 - 110) * 255).toInt)
        } else if (longeur_Onde < 200) {
            new Color(((longeur_Onde - 130) / (200 - 130) * 255).toInt, 255, 0)
        } else if (longeur_Onde < 265) {
            new Color(255, (-(longeur_Onde - 265) / (265 - 200) * 255).toInt, 0)
        } else 
            new Color(255, 0, 0)
        
    }
}