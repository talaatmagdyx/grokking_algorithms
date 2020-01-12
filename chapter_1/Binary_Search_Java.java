public class Binary_Search_Java{
	public static Integer Binary_search(int list [], int target_search ){
		int low  = 0;
		int high =  list.length -1;
		while (low <= high){
			int mid = (low + high) / 2;
			int guess = list[mid];

			if(guess == target_search){
				return mid;
			}else if (guess < target_search ){
				low = mid + 1 ;
			}else{
				high = mid -1;
			}
		}
		return null;

	}
    public static void main ( String args []){
    	int my_list [] = {1,2,3,4,5,6};
    	System.out.print(Binary_search(my_list, 3));
    }
}
