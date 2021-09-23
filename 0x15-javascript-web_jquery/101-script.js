window.addEventListener('DOMContentLoaded', () => {
  const addItem = $('DIV#add_item');
  const myList = $('.my_list');
  $(addItem).click(function () {
    myList.append('<li>Item</li>');
  });

  const clearItem = $('DIV#clear_list');
  const myList2 = $('.my_list');
  $(clearItem).click(function () {
    myList2.text('');
  });

  const removeItem = $('DIV#remove_item');
  const myList3 = $('.my_list');
  $(removeItem).click(function () {
    myList3.children().last().remove();
  });
});
