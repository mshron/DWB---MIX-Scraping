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
, "parse":function(){
    branch_nodes=$('select[name="Centralcolum3$drpFAQ"] option');
    var branches={}
    branch_nodes.each(function(){
      var branch_id=$(this).attr('value');
      var branch_name=$(this).text();
      branches[branch_id]=branch_name;
//      console.log([branch_id,branch_name]);
    });
//    console.log(branches);
    $('select[name="Centralcolum3$drpFAQ"]').val('333');
    $('#Centralcolum3_btnSubmit').click();
  }
, "scrape":function(callback){
  }
}

jQuery(function(){
  chainsaw.parse();
});
