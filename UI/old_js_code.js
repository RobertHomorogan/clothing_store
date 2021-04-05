async function getFirstUser() {
	const request = new Request('http://localhost:5000/get_first_user');
	fetch(request)
		.then(response => response.text())
		.then(user => {
			console.log(user);
			document.getElementById('first_user').innerHTML = `The first user is: ${user}`
		}).catch(error => console.warn(error));
}
