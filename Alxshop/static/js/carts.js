var updateButns = document.getElementsByClassName('update-carts')

for(var i= 0; i < updateButns.length; i++){
    updateButns[i].addEventListener('click', function(){
        var productId= this.dataset.product
        var action= this.dataset.action
        console.log('productId:', productId, 'action:', action)

        console.log('USER:', user)

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
        if (cart[productId] == undefined){
            cart[productId] = {'quantity':1}
        }else{
            cart[productId]['quantity'] += 1
        }
        


    }
    if (action == 'remove'){
        cart[productId]['quantity'] -= 1
        if (cart[productId]['quantity'] <= 0){
            console.log('item shoulld be deleted')
            delete cart[productId]
        }
    }
    console.log('cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
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
