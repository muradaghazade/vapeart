ids = JSON.parse(localStorage.getItem('products'))
    
    data = {
        ids:ids
    }

    fetch('/api/products/', {
        method: "POST",
        headers: {
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUxMjM4OTM0LCJpYXQiOjE2NDg2NDY5MzQsImp0aSI6IjI5MTY4N2FjMDEyNTRiZjQ4YzlmY2FhNzQwM2ViZGMwIiwidXNlcl9pZCI6NiwidXNlcm5hbWUiOm51bGwsImVtYWlsIjoic3RvcmVtYWlsQGdtYWlsLmNvbSJ9.W_TeYd-1pufSsMKs5KasRN5O0R0e81DBbCHc_3UyPLQ",
            "Content-type": "application/json",
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data),
      })
        .then((resp) => resp.json())
        .then((data) => {
          price = 0
          console.log(data);
          data.forEach(element => {
              price+=parseInt(element.price)
            document.getElementById('prod_table').innerHTML += 
            `<tr>
                          <td style="border-bottom: 1px #dee2e6 solid">
                            <img
                              width="60"
                              src="${element.images[0].image}"
                            />
                          </td>
                          <td
                            style="width: 55%; border-bottom: 1px #dee2e6 solid"
                          >
                            <p>
                              <a href="/-eleaf-ijust-3-3000-mah/"
                                >${element.title}</a
                              >
                            </p>
                          </td>
                          <td
                            style="
                              width: 75px;
                              min-width: 75px;
                              border-bottom: 1px #dee2e6 solid;
                            "
                          >
                            
                            <input
                              class="product-id"
                              name="PRODUCT_ID"
                              type="hidden"
                              value="300261"
                            />
                            <input
                              class="product-id-db"
                              name="PRODUCT_ID_DB"
                              type="hidden"
                              value="17718"
                            />
                          </td>
                          <td style="border-bottom: 1px #dee2e6 solid">
                            <p class="product-price">
                              <b><nobr>${element.price} AZN</nobr></b>
                            </p>
                          </td>
                          <td class="td_delete" style="border-bottom: 1px #dee2e6 solid">
                            <input
                              id="delete-item-basket-300261"
                              class="delete-item-basket"
                              type="button"
                              data="300261"
                              title="Mehsul sebetden silinsin?"
                              value=""
                              data-toggle="modal"
                              data-target="#confirm-delete-item-basket"
                            />
                            <i class="fa-solid fa-xmark" id="remove" productid="${element.id}"></i>
                          </td>
                        </tr> `
          });
          document.getElementById("final_price").innerText = `${price} AZN`
          document.getElementById("price-form").value = price
        })



document.addEventListener('click', e => {
    if (e.target.getAttribute('id') == 'remove') {
        products = JSON.parse(localStorage.getItem('products'))
        const index = products.indexOf(parseInt(e.target.getAttribute('productid')));
        if (index > -1) {
            products.splice(index,1); // 2nd parameter means remove one item only
        }
        localStorage.setItem('products', JSON.stringify(products))
        e.target.parentElement.parentElement.style.display = 'none'
    }
})


document.getElementById("clearall").addEventListener('click', e => {
    localStorage.clear()
    document.getElementById('prod_table').style.display = 'none'
})