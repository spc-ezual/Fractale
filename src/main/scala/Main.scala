import mathematiques.Complexe
import outils.Triangle
import outils.Dragon

object Main extends App {
  val c1 = new Complexe(3, 4)
  val c2 = new Complexe(1, 2)

  println(s"c1 = $c1")
  println(s"c2 = $c2")

  val addition = c1 + c2
  val soustraction = c1 - c2
  val multiplication = c1 * c2
  val division = c1 / c2

  println(s"Addition : $addition")
  println(s"Soustraction : $soustraction")
  println(s"Multiplication : $multiplication")
  println(s"Division : $division")

  println(s"Norme de c1 : ${c1.norme}")
  println(s"Conjugé de c2 : ${c2.conjuguer}")

  val racineCarreeC1 = c1.racineCarree
  val racineCarreeC2 = c2.racineCarree

  println(s"Racine carrée de c1 : $racineCarreeC1")
  println(s"Racine carrée de c2 : $racineCarreeC2")

  val cosinusC1 = c1.cosinus
  val sinusC2 = c2.sinus

  println(s"Cosinus de c1 : $cosinusC1")
  println(s"Sinus de c2 : $sinusC2")

  println("-------------------------------------")
  var a = Triangle;
  a.generateSierpinski(1000,1000,5,true,"test",(100,100,100),(200,200,200))
  var b = Dragon
  b.generateDragon(3000,3000,10,(0,0,0),(200,200,200),"test",-1)
}
