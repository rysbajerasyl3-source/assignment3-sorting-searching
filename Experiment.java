public class Experiment {
    private Sorter sorter = new Sorter();
    private Searcher searcher = new Searcher();

    public long measureSortTime(int[] arr, String type) {
        int[] copy = arr.clone();
        long start = System.nanoTime();
        if (type.equals("basic"))
            sorter.basicSort(copy);
        else
            sorter.advancedSort(copy);
        long end = System.nanoTime();
        return end - start;
    }

    public long measureSearchTime(int[] arr, int target) {
        long start = System.nanoTime();
        searcher.search(arr, target);
        long end = System.nanoTime();
        return end - start;
    }

    public void runAllExperiments() {
        int[] sizes = {10, 100, 1000};
        for (int size : sizes) {
            System.out.println("\nArray size: " + size);
            int[] randomArray = sorter.generateRandomArray(size);

            long basicTime = measureSortTime(randomArray, "basic");
            long advancedTime = measureSortTime(randomArray, "advanced");

            sorter.advancedSort(randomArray);
            int target = randomArray[size / 2];
            long searchTime = measureSearchTime(randomArray, target);
            System.out.println("Insertion Sort time: " + basicTime);
            System.out.println("Merge Sort time: " + advancedTime);
            System.out.println("Binary Search time: " + searchTime);
        }
    }
}