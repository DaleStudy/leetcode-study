import scala.collection.mutable.ArrayBuffer

object Solution {
    var encoder = "(){}[]".zipWithIndex
            .toMap
    def isValid(s: String): Boolean = {
        val arr = ArrayBuffer[Int]()
        s.forall { c =>
                    val x = encoder(c)
                    if ((x & 1) == 0) {
                        arr += x
                        true
                    } else {
                        arr.lastOption match {
                            case Some(y) => {
                                if (y == x - 1) {
                                    arr.dropRightInPlace (1)
                                    true
                                } else false
                            }
                            case None => false
                        }
                    }
                } && arr.isEmpty
    }
}
