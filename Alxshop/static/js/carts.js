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
            console.log('user is logged in, sending data')
        }

    })
}