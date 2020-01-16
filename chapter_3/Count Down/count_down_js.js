const countdown = x =>{
	console.log(x);
	if (x <= 0){
		return ;
	}else{
		countdown(x-1);
	}
};

countdown(3);