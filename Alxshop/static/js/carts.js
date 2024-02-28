var updateBtns = document.getElementsByClassName('update-cart')

for(var i= 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.Log('productId:', productId, 'action:', action)

        console.Log('USER:', user)  

        if(user === 'AnonymousUser'){
            console.log('Not logged in')

        }else{ 
            updateUserOrder(productId, action)
        }

    })
}
function addCookieItem(productId, action){
    console.log('user is not authenticated')

    if (action == 'add'){
        if (carts[productId] == undefined){
            carts[productId] = {'quantity':1}
        }else{
            carts[productId]['quantity'] += 1
        }
        


    }
    if (action == 'remove'){
        carts[productId]['quantity'] -= 1
        if (carts[productId]['quantity'] <= 0){
            console.log('item shoulld be deleted')
            delete carts[productId]
        }
    }
    console.log('carts:', carts)
    document.cookie = 'carts=' + JSON.stringify(carts) + ";domain=;path=/"
    location.reload()
}
function updateUserOrder(productId, action) {
    console.Log('User is logged in, sending data..')

    var url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
         
        body:JSON.stringify({'productId': productId, 'action':action})
    })


    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.Log('data:', data)
    })
}

