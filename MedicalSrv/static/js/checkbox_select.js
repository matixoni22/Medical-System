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

   function updateTextArea() {         
        var allVals = [];
        $("input[name='check']:checked").each(function() {
        allVals.push($(this).val());
        });
        $('#inp_img').val(allVals);
    }
    
    $(function() {
    $("input[name='check']").change(updateTextArea);
    updateTextArea();
    }); 


 });