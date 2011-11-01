chainsaw={
  "push":function(rows,callback){
    docs=JSON.stringify({"docs":rows});
    jQuery.ajax({
      url: 'http://chainsaw.iriscouch.com/postbank/_bulk_docs'
    , type: 'POST'
    , data: docs
    , dataType: 'json'
    , contentType: "application/json; charset=utf-8"
    , success: function(res) {console.log(res);}
    });
    if (typeof(callback)==="function"){
      callback();
    }
  }
, "grab":function(){
    selected=$('select[name="Centralcolum3$drpFAQ"] option:selected');
    next_val=selected.next().val();
    if (next_val!="Please select..."){
      $('select[name="Centralcolum3$drpFAQ"]').val(next_val);
      $('#Centralcolum3_btnSubmit').click();
    }
  }
}

jQuery(function(){
  chainsaw.grab();
});
