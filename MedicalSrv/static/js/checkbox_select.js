$(document).ready(function () {
    $("input[name='check']").change(function () {
       var maxAllowed = 2;
       var cnt = $("input[name='check']:checked").length;
       if (cnt > maxAllowed) 
       {
          $(this).prop("checked", "");
          alert('Select ' + maxAllowed + ' images for alanalyse!');
      }
   });
       
   $("input[name='selection']").change(function() {
        $("input[name='selection']").not(this).prop('checked', false);  
    });
    window.allVals = [];
   function updateTextArea(value) {         
        var r = value.currentTarget;
        if(r.checked == true)
        {
           allVals.unshift(r.defaultValue);
        }
        else{
            allVals = $.grep(allVals, function(value) {
                return value != r.defaultValue;
              });
        }
        $.unique(allVals);
        $('#inp_img').val(allVals);
    }
    
    $(function() {
    $("input[name='check']").change(updateTextArea);
    updateTextArea(this);
    }); 


 });