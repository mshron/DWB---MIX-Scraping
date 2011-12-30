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
, "parse":function(){
    basepath='#Centralcolum3_dtgGroup td > '
    cell_nodes=$(basepath+'span , '+basepath+'strong');
    d=this.makerow(cell_nodes);
    return d;
  }
, "makerow":function(cell_nodes){
    cells=[]
    cell_nodes.each(function(){
      cells.push($(this).text());
    });
    d={};
    cells.pop(); //Remove that junk '1' at the end
    //Go backwards because pop comes from the end.
    while (cells.length>2){
      value=this.getcellvalue(cells);
      key=this.getcellvalue(cells);
      d[key]=value;
    }
    d['loc2']=this.getcellvalue(cells);
    d['loc1']=this.getcellvalue(cells);
    return d;
  }
, "getcellvalue":function(cells){
    return this.compact(cells.pop(0));
  }
, "compact":function(str){
/*
    str=str.replace('\n',' ');
    str=str.replace('  +','').replace('^ *','').replace(' *$','');
*/
    return str;
  }
}

jQuery(function(){
  d=chainsaw.parse();
  chainsaw.push([d]);
  chainsaw.grab();
});
