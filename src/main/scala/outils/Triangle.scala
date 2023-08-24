package outils
import java.awt.image.BufferedImage
import java.io.File
import javax.imageio.ImageIO
import java.awt.Color

object Triangle{
    /**
      * 
      *
      * @param a coordonner du point a
      * @param b coordonner du point b
      * @return coordonner du point entre a et b
      */
    def millieu(a : (Int,Int),b : (Int,Int)):(Int,Int)={
        return ((a._1+b._1)/2,(a._2+b._2)/2)
    }
    /**
      * 
      *
      * @param h hauteur
      * @param l largeur
      * @param i nombres d'iteration
      * @param equi boolean de si equilateral ou non 
      * @param nom nom du fichier
      * @param font couleur de font en rgb
      * @param couleur couleur de l'image en rgb
      */
    def generateSierpinski(l : Int , h :Int, i : Int, equi : Boolean, nom : String , font : (Int,Int,Int),couleur : (Int,Int,Int)){
        var a,b,c :(Int,Int)=(0,0);
        if(equi){
            //TODO 3 cas si h<l , h>l , h=l peut etre que h=l <=> h>l ???
            a = (l/2,0)
            b = (l-1,h-1)
            c = (0,h-1)
        }else{
            a = (l/2,0)
            b = (l-1,h-1)
            c = (0,h-1)
        }
        val image = new BufferedImage(l, h, BufferedImage.TYPE_INT_RGB)
        val graphics = image.createGraphics()

        graphics.setColor(new Color(font._1,font._2,font._3))
        graphics.fillRect(0, 0, l, h)

        graphics.dispose()
        creationTriangle(image,a,b,c,i,new Color(couleur._1,couleur._2,couleur._3))
        val outputFile = new File(nom+".jpg")
        ImageIO.write(image, "jpg", outputFile)
        println(s"Image '$nom' créée avec succès.")
    }
    /**
      * 
      *
      * @param imageimage sur la quelle tracer les triangle
      * @param a coordonner du point a
      * @param b coordonner du point a
      * @param c coordonner du point a
      * @param i nombre d'iteration
      * @param couleur couleur de la figure
      */
    def creationTriangle(image : BufferedImage,a:(Int,Int),b:(Int,Int),c:(Int,Int),i :Int,couleur:Color){
        if(i==0){
            val graphics = image.createGraphics()
            graphics.setColor(couleur)
            graphics.fillPolygon(Array(a._1, b._1, c._1),
                        Array(a._2, b._2, c._2),
                        3)
            graphics.dispose()
        }else{
            val d = millieu(a,b)
            val e = millieu(c,b)
            val f = millieu(a,c)
            creationTriangle(image,a,d,f,i-1,couleur)
            creationTriangle(image,d,b,e,i-1,couleur)
            creationTriangle(image,f,c,e,i-1,couleur)
        }
        
    }
}