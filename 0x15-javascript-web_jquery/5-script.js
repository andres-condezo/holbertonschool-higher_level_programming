const addItem = $('DIV#add_item');
const myList = $('.my_list');
$(addItem).click(function () {
  myList.append('<li>Item</li>');
});
