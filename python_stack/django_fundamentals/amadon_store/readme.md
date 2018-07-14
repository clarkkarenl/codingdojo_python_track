Assignment: Amadon
Karen Clark
2018-07-13

Topics

* Session and Post Handling
* Mixing post handling with html render - why this should be avoided
* Basic security - why you should be careful about what you put inside <form>

You've decided to build your own e-commerce site called Amadon and decide to make this into a Django app.  Without creating anything in the database (which you'll learn later), have the app remember what items you've purchased so far.  

Once your customer bought the item, say your customer reloaded the page.  Would your customer be happy if your app re-orders the same product and charges his/her credit card again?  Probably not!  Make sure your app doesn't charge the card again when the customer reloads the 'checkout' page ('checkout' page defined as localhost/amadon/checkout where they see a thank you message).

IMPORTANT LESSON 1: This is why you (as a good developer) should not have the method handle both the POST data and render HTML.  In fact, this is such a common mistake made by lots of developers that you should keep an eye and try not to make this mistake yourself. Instead, for example, have the http request sent to '/amadon/buy' handle the POST data and have it redirect to '/amadon/checkout' which displays the thank you html.  This way, even when the user reloads the thank you page, it would not re-process the submitted order.

For this assignment, either create your own CSS file or  use Twitter Bootstrap.

IMPORTANT LESSON 2: One reason we designed this assignment is for you to see how easy it is to manipulate the form.  For example, say that the form for ordering a Dojo T-shirt looked like this.
```
<form action='/amadon/buy' method='post'>
  {% csrf_token %}
  <select name='quantity'>
     <option>1</option>
     <option>2</option>
     <option>3</option>
  </select>
  <input type='hidden' name='price' value='19.99' />
  <input type='submit' value='Buy!' />
</form>
```

A somewhat sophisticated user could, for example, use Inspect Element to change the price to '0.01' and order lots of T-shirts for very cheap!  A better way to handle this would be to have for example product_id as a hidden variable.  This way, if they change the product_id using inspect element, they would just get a different item for their order.

In other words, have the form look more like below:
```
<form action='/amadon/buy' method='post'>
  {% csrf_token %}
  <select name='quantity'>
     <option>1</option>
     <option>2</option>
     <option>3</option>
  </select>
  <input type='hidden' name='product_id' value='1015' />
  <input type='submit' value='Buy!' />
</form>
```

Surprisingly, a lot of e-commerce sites are built where you could easily change the price.  What if you built a web crawler/scraper to go through lots of e-commerce sites to specifically look for sites where price is part of the shopping cart form?  You could order lots of items for very cheap (although you'll probably get caught) or also reach out to them and tell them about the security flaw in their site.  Maybe they'll hire you to make their site more secure? :)