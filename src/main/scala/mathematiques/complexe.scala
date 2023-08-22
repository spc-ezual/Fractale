package mathematiques

class Complexe(val re: Double, val im: Double) {
  override def toString: String = {
    if (re == 0 && im == 0) "0"
    else if (re != 0 && im == 0) s"$re"
    else if (re == 0 && im > 0) s"$im" + "i"
    else {
      val signei = if (im > 0) " + " else " - "
      s"$re$signei${math.abs(im)}i"
    }
  }

  def +(b: Complexe): Complexe = new Complexe(b.re + re, b.im + im)
  def -(b: Complexe): Complexe = new Complexe(re - b.re, im - b.im)
  def *(b: Complexe): Complexe =
    new Complexe(re * b.re - im * b.im, im * b.re + re * b.im)
  def /(comp: Complexe): Complexe = {
    val denom = comp.re * comp.re + comp.im * comp.im
    new Complexe(
      (re * comp.re + im * comp.im) / denom,
      (-re * comp.im + im * comp.re) / denom
    )
  }
  def +(b: AnyVal): Complexe = b match {
    case num: Double => new Complexe(num + re, im)
    case num: Int    => new Complexe(num + re, im)
    case num: Byte   => new Complexe(num + re, im)
    case num: Short  => new Complexe(num + re, im)
    case num: Long   => new Complexe(num + re, im)
    case num: Float  => new Complexe(num + re, im)
    case _ =>
      throw new IllegalArgumentException("Opération non prise en charge")
  }

  def -(b: AnyVal): Complexe = b match {
    case num: Double => new Complexe(re - num, im)
    case num: Int    => new Complexe(re - num, im)
    case num: Byte   => new Complexe(re - num, im)
    case num: Short  => new Complexe(re - num, im)
    case num: Long   => new Complexe(re - num, im)
    case num: Float  => new Complexe(re - num, im)
    case _ =>
      throw new IllegalArgumentException("Opération non prise en charge")
  }

  def *(b: AnyVal): Complexe = b match {
    case num: Double => new Complexe(re * num, im * num)
    case num: Int    => new Complexe(re * num, im * num)
    case num: Byte   => new Complexe(re * num, im * num)
    case num: Short  => new Complexe(re * num, im * num)
    case num: Long   => new Complexe(re * num, im * num)
    case num: Float  => new Complexe(re * num, im * num)
    case _ =>
      throw new IllegalArgumentException("Opération non prise en charge")
  }

  def /(b: AnyVal): Complexe = b match {
    case num: Double =>
      new Complexe(re / num, im / num)
    case num: Int =>
      new Complexe(re / num, im / num)
    case num: Byte =>
      new Complexe(re / num, im / num)
    case num: Short =>
      new Complexe(re / num, im / num)
    case num: Long =>
      new Complexe(re / num, im / num)
    case num: Float =>
      new Complexe(re / num, im / num)
    case _ =>
      throw new IllegalArgumentException("Opération non prise en charge")
  }

  def estReel: Boolean = im == 0
  def estImaginaire: Boolean = re == 0
  def partieReel: Double = re
  def partieImaginaire: Double = im

  def racineCarree: Complexe = {
    var y = new Complexe(1, 0)
    for (_ <- 0 until 500) {
      y = new Complexe(0.5, 0) * (y + (this / y));
    }
    y
  }

  def norme: Double = math.sqrt(re * re + im * im)
  def conjuguer: Complexe = new Complexe(re, -im)
  def cosinus: Complexe =
    new Complexe(math.cos(re) * math.cosh(im), -math.sin(re) * math.sinh(im))
  def sinus: Complexe =
    new Complexe(math.sin(re) * math.cosh(im), math.cos(re) * math.sinh(im))
  def cosinusH: Complexe =
    new Complexe(math.cosh(re) * math.cos(im), math.sinh(re) * math.sin(im))
  def sinusH: Complexe =
    new Complexe(math.sinh(re) * math.cos(im), math.cosh(re) * math.sin(im))
  def carre: Complexe = new Complexe(re * re - im * im, 2 * re * im)
}
