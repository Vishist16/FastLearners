
$(document).ready(function(){
    load_data();
    function load_data(query='')
    {
        $.ajax({
            url:"/sdata",
            method:"POST",
            data:{query:query},
            success:function(data)
            { 
                $('tbody').html(data);
                $('tbody').append(data.htmlresponse);
            }
        })
    }
 
    $('#search_home').change(function(){
        $('#hidden_home').val($('#search_home').val());
        var query = $('#hidden_home').val(); 
        load_data(query);
    });
     
});
