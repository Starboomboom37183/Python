/*************************************************************************
    > File Name: test1.c
    > Author: WangYong
    > Mail: 1558448539@qq.com 
    > Created Time: 2018-09-09
 ************************************************************************/

#include<stdio.h>
#include<string.h>
#include<limits.h>
int main(){
	char a[1000];
	int i;
	for(int i=0;i<1000;++i){
		a[i] = -1-i; 
	}
    int b=0;
	int c =1;
	int temp = b+++c;
	printf("temp is %d\n",temp);
	//haha
/*************************************************************************
    > File Name: test1.c
    > Author: WangYong
    > Mail: 1558448539@qq.com 
    > Created Time: 2018-09-09
 ************************************************************************/
   int m = (0,1);
   printf("m = %d\n",m);
   printf("INT_MAX is %d\n",INT_MAX);
	char *s = "abcdefgh //hijklmn";
	//双引号内部的都是字符串常量
	printf("%s\n",s);
	printf("%d\n",(int)strlen(a));
	printf("%d\n",sizeof(a));
	return 0;/*************************************************************************
    > File Name: test1.c
    > Author: WangYong
    > Mail: 1558448539@qq.com 
    > Created Time: 2018-09-09
 ************************************************************************/
}
