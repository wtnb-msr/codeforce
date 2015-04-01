import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.BitSet;

public class Solver {

  BufferedReader reader;
  BufferedWriter writer;

  public void setup() throws Exception {
    reader = new BufferedReader(new InputStreamReader(System.in));
    writer = new BufferedWriter(new OutputStreamWriter(System.out));
  }

  public void cleanup() throws Exception {
    reader.close();
    writer.flush();
    writer.close();
  }

  public String readLine() throws Exception {
    return reader.readLine();
  }

  public void println(String text) throws Exception {
    writer.write(text);
    writer.newLine();
  }

  public int getMaximumLength(BitSet positionSet) {
    int preIndex = 0;
    int maxLength = 0;
    for (int index = positionSet.nextSetBit(1); index >= 0; index = positionSet.nextSetBit(index + 1)) {
      int length = index - preIndex;
      if (length > maxLength) {
        maxLength = length;
      }
      preIndex = index;
    }
    return maxLength;
  }

  public void solve() throws Exception {
    String[] token = readLine().split(" ");
    int width = Integer.parseInt(token[0]);
    int height = Integer.parseInt(token[1]);
    int numCuts = Integer.parseInt(token[2]);

    BitSet horizontalPositionSet = new BitSet(height + 1);
    BitSet verticalPositionSet = new BitSet(width + 1);
    horizontalPositionSet.set(0);
    horizontalPositionSet.set(height);
    verticalPositionSet.set(0);
    verticalPositionSet.set(width);

    for (int i = 0; i < numCuts; i++) {
      token = readLine().split(" ");
      String cutType = token[0];
      int cutPosition = Integer.parseInt(token[1]);

      if (cutType.equals("H")) {
        horizontalPositionSet.set(cutPosition);
      } else if (cutType.equals("V")) {
        verticalPositionSet.set(cutPosition);
      }

      int maxWidth = getMaximumLength(verticalPositionSet);
      int maxHeight = getMaximumLength(horizontalPositionSet);
      int maxSquare = maxWidth * maxHeight;
      println(Integer.toString(maxSquare));
    }
  }

  public static void main(String[] args) {
    try {
      Solver solver = new Solver();
      solver.setup();
      solver.solve();
      solver.cleanup();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
