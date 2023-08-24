name := "Fractale"
version := "0.1"

scalaVersion := "2.13.5"

libraryDependencies ++= Seq(
  "org.scala-lang.modules" %% "scala-swing" % "2.1.1",
  "junit" % "junit" % "4.12" % Test,
  "com.novocode" % "junit-interface" % "0.11" % Test exclude ("junit", "junit-dep"),
  "org.apache.commons" % "commons-text" % "1.9",
  // Twelvemonkeys ImageIO
  "com.twelvemonkeys.imageio" % "imageio-core" % "3.9.4",

  // OpenCV
  "org.bytedeco" % "javacv" % "1.5.5" // Includes OpenCV bindings
)
