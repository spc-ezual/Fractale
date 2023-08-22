package application

import scala.swing.SimpleSwingApplication
import scala.swing.MainFrame

object Fractale extends SimpleSwingApplication {
    val ui = new UI

    def top: MainFrame = ui

}