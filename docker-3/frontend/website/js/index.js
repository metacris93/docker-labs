const options = {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    },
    redirect: 'follow'
}

// fetch("http://backend:5000/api/getMyInfo", options)
fetch("http://localhost:5000/api/getMyInfo", options)
    .then(response => {
        if (!response.ok) {
            alert("Error -> " + response.status)
        }
        return response.json()
    })
    .then(data => {
        document.getElementById("name").textContent = `${data.name} ${data.lastname}`
        document.getElementById("author").textContent = `2023 - Hecho por ${data.author}`
        document.getElementById("facebookLink").href = `https://www.facebook.com/${data.socialMedia.facebookUser}`
        document.getElementById("instagramLink").href = `https://instagram.com/${data.socialMedia.instagramUser}`
        document.getElementById("twitterLink").href = `https://x.com/${data.socialMedia.xUser}`
        document.getElementById("githubLink").href = `https://github.com/${data.socialMedia.githubUser}`
        document.getElementById("linkedinLink").href = `https://linkedin.com/${data.socialMedia.linkedin}`
        document.getElementById("website").href = `https://linkedin.com/${data.blog}`
    })
    .catch(error => alert('error: ' + error));