$(document).ready(function(){
            
    $(".deleteButton").on('click',function(){
        $("#deleteModel").modal('show');

        $tr=$(this).closest('tr')

        var data=$tr.children("td").map(function(){
            return $(this).text()
        }).get()

        var contact_id=$('#delete_id').val(data[0])
        console.log(data[0])

        
        
});
});

            
   
        
        
