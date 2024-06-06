let projecturl='http://127.0.0.1:8000/api/project'

let getproject=async()=>{
    data=await(fetch(projecturl))
    json=await(data.json())
    console.log(json)
    buildProject(json)
}

let buildProject=(x)=>{
    let projectcontainer=document.getElementById('container')
    for(let i=0;x.length>i;i++)
    {
        let project=x[i]
        let projectcard=`
        <div>
            <img src="http://127.0.0.1:8000${project.image}">
            <div>
                <p>${project.title}</p>
                <p>${project.Vote_ratio}</p>
            </div>
            <div>
            <button><a href="{% url 'updateproject' i.id %}">Update</a></button>
            <button><a href="{% url 'deleteproject' i.id %}">Delete</a></button>
            </div>
        </div>`
        projectcontainer.innerHTML+=projectcard
    }
}

getproject()