package outils
import java.awt.image.BufferedImage
import java.io.File
import javax.imageio.ImageIO
import java.awt.Color

object Dragon{
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

    def generateDragon(l : Int,h : Int,i :Int , fond : (Int,Int,Int),coul : (Int,Int,Int),nom : String , sense : Int ){
        val a =((l/4).toInt,h/2)
        val b = ((l*0.75).toInt,h/2)
        val image = new BufferedImage(l,h,BufferedImage.TYPE_INT_RGB)
        val graphics = image.createGraphics()
        
        graphics.setColor(new Color(fond._1,fond._2,fond._3))
        graphics.fillRect(0,0,l,h)
        graphics.dispose()

        iterationCourbe(image,a,b,sense,i,new Color(coul._1,coul._2,coul._3))

        val outFile= new File(nom+".jpg")
        ImageIO.write(image,"jpg",outFile)
        println(s"Image '$nom' créée avec succès.")

    }

    def iterationCourbe(image : BufferedImage, a : (Int,Int) , b : (Int,Int),sense : Int,i :Int , couleur :Color){
        if(i == 0){
            val graphics = image.createGraphics()
            graphics.setColor(couleur)
            graphics.drawLine(a._1,a._2,b._1,b._2)
            graphics.dispose()
        }else{
            val imageDeB = ((a._1+sense*(a._2-b._2)),(a._2+sense*(b._1-a._1)))
            val c = millieu(imageDeB,b)
            iterationCourbe(image,a,c,1,i-1,couleur)
            iterationCourbe(image,c,b,-1,i-1,couleur)
        }
    }

}
