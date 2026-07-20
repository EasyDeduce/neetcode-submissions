class Solution {
    public int firstMissingPositive(int[] nums) {
        int l= nums.length;
        int max=-1;
        int min=1000000;
        for (int i=0; i<l; i++){
            if (nums[i]>=0 && nums[i]>max){
                max= nums[i];
            }
            if (nums[i]>=0 && nums[i]<min){
                min=nums[i];
            }
        }
        int initmax=max;
        int maxfrommax=min;
        int minfrommin=max;
        int i=0;
        int t1=0;
        int t2=0;
        if (min>1){
            return 1;
        }
        while (true){ 
            System.out.print(nums[i]+ " "+ min+ " "+ max +" " + minfrommin + " " + maxfrommax);
            if (nums[i]>0 && nums[i]>min && nums[i]<max && nums[i]>maxfrommax){
                System.out.print(" a");
                maxfrommax=nums[i];
            }
            if (nums[i]>0 && nums[i]<max && nums[i]>min && nums[i]<minfrommin){
                minfrommin=nums[i];
                System.out.print(" b");
            }
            if (i==l-1 && minfrommin==t2 && maxfrommax==t1){
                System.out.print(" n");
                return initmax+1;
            }
            if (i==l-1 && minfrommin!=min+1){
                System.out.print(" c");
                return min+1;
            }
            i++;
            if (i==l && minfrommin!=maxfrommax){
                t1=min;
                t2= max;
                min= minfrommin;
                max= maxfrommax;
                minfrommin=t2;
                maxfrommax=t1;
                i=0;
                System.out.print(" d");
            }
            if (i==l && minfrommin == maxfrommax && maxfrommax+1==max){
                System.out.print(" e");
                return initmax+1;
            }
            if (i==l && minfrommin==maxfrommax && maxfrommax+1!=max){
                System.out.print(" f");
                return maxfrommax+1;
            }
            System.out.println();
        }
    }
}