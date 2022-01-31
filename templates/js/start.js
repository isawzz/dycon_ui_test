window.onload = start; 

async function start() {

	let dMain = mBy('dMain');
	mCenterFlex(dMain);

	let dForm = mBy('dForm');
	mStyleX(dForm,{matop:20})

	let dStatus = mDiv(dMain,{matop:25,fg:'red'},'dStatus','wirklich? so einfach geht das???');
}
