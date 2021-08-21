/* globals Chart:false, feather:false */


// Functions

(function () {
  'use strict'

  feather.replace({ 'aria-hidden': 'true' })


})()

function convertToSlug(Text)
{
    return Text
        .toLowerCase()
        .replace(/[^\w ]+/g,'')
        .replace(/ +/g,'-')
        ;
}


// Admin Hooks

function fillSlugHook() {
  let titleInputValue = document.querySelector('input#title').value;
  let slugInput = document.querySelector('input#slug').value = convertToSlug(titleInputValue);

}


