let modalPostDelete = document.querySelector('.modalPostDelete')
let btnDelete = document.querySelector(".btnDelete")
let modalPostDelete_bg = document.querySelector('.modalPostDelete_bg')



btnDelete.addEventListener('click', function(){
	modalPostDelete.classList.add('show');
	modalPostDelete_bg.classList.add('show');

})