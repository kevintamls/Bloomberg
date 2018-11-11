//Tam Kevin Lok Sun, 1742270
//Import List, Arraylist, BufferedReader, FileReader, Scanner
import java.util.List;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Scanner;

//Define Class SortingAlgorithms
class SortingAlgorithms {
  //Define method bubbleSort
	public static void bubbleSort(List<String> list, int n) {

    //Variables to count moves and swaps
    int moves = 0;
    int swaps = 0;

		for (int i = 1; i < n - 1; i++) { //Outer For loop
      for (int j = 1; j < n - i; j++) { //Inner for loop
        moves++;
        if (list.get(j + 1).compareTo(list.get(j)) < 0) { //if statement
          swaps++; //Add 1 to swaps
          String temp = list.get(j);
          list.set(j, list.get(j +1));
          list.set(j + 1, temp);
        }
      }
    }
    //Prints number of moves and swaps performed
    System.out.println("Number of comparisons performed = " + moves);
    System.out.println("Number of swaps performed = " + swaps);
  }

  //Define method mergeSort
  public static void mergeSort(List<String> list) {
    //Condition Check for amount of elements less or equal to 1. No sorting required.
    if (list.size() <= 1) {
        return;
    }

    //Variable to determaining middle of ArrayList
    int half = (int) (list.size() / 2);
    //Initialize 2 seperate Subarrays, containing elements 0 to half and half to last element of initial arrayList.
    List<String> firstHalf = new ArrayList<String>(list.subList(0, half));
    List<String> secondHalf = new ArrayList<String>(list.subList(half, list.size()));

    //Run function merge sort
    mergeSort(firstHalf);
    mergeSort(secondHalf);

    //Run merge function
    merge(firstHalf, secondHalf, list);
    System.out.println("Number of comparisons performed = " + whileloop);

    //Return staement
    return;
  }

  //Define method merge
  public static void merge(List<String> firstHalf, List<String> secondHalf, List<String> result) {
    //Initialize int variables firstHalfPos, secondHalfPos, resultPos
    int firstHalfPos = 0;
    int secondHalfPos = 0;
    int resultPos = 0;


    //While loop
    while (firstHalfPos < firstHalf.size() && secondHalfPos < secondHalf.size()) {
      //If statement
      if (firstHalf.get(firstHalfPos).compareTo(secondHalf.get(secondHalfPos)) < 0) {
        result.set(resultPos, firstHalf.get(firstHalfPos));
        //Adds 1 to amount of elements in firstHalf
        firstHalfPos++;
      }
      else {
        result.set(resultPos, secondHalf.get(secondHalfPos));
        //Adds 1 to amount of elements in secondHalf
        secondHalfPos++;
      }
      //Adds 1 to amount of elements in result
      resultPos++;
    }
    //For loop, moves remaining elements in firstHalf array to result array
    for (int i = firstHalfPos; i < firstHalf.size(); i++) {
      result.set(resultPos, firstHalf.get(i));
      resultPos++;
    }
  }

  public static void main(String args[]) throws Exception {

    //Scanner to parse number of words to be sorted
    Scanner reader = new Scanner(System.in);
    System.out.println("Enter number of words: ");
    int n = reader.nextInt();
    System.out.println("Enter 0 for Bubble Sort, 1 for Merge Sort");
    int sort = reader.nextInt();
		// Create array list
		List<String> list = new ArrayList<String>();

    //Define variables line for linechecking
    String line;
    //Read File
    BufferedReader bufReader = new BufferedReader(new FileReader("data.txt"));
    //While Loop
      while ((line = bufReader.readLine()) != null) {
        String test = bufReader.readLine();//Read Line
        String[] splitTest = test.replaceAll("[^a-zA-Z ]", "").replaceAll("\\b[\\w']{1,2}\\b", "").toLowerCase().split("\\s+");//Remove non-word char, remove strings with less than 3 characters

        //For loop for arrayList size limit
        for (String a : splitTest) {;
          if(list.size() > n) {
            break;
          }
          else {
            list.add(a);
            }
          }
        }

    //Timer
		long averageTime = 0L;

    //For loop to run 10 times
    for (int i = 0; i < 10; i++) {
      List<String> listArg = new ArrayList<>(list);
      long start = System.nanoTime();

      // Run the sort
      if (sort == 0) {
        SortingAlgorithms.bubbleSort(listArg, listArg.size());
      }
      if (sort == 1) {
        SortingAlgorithms.mergeSort(listArg);
      }

      //End Timer
      long end = System.nanoTime();
      long timeTaken = end - start;
      System.out.println("Time taken = " + timeTaken);
      averageTime += timeTaken;

		}

		// Print out average time
		averageTime /= 10;
		System.out.println("Average time taken = " + averageTime);


	}

}
