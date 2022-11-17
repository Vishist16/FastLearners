
$(document).ready(function(){
    load_data();
    function load_data(query='')
    {
        $.ajax({
            url:"/fetchrecords",
            method:"POST",
            data:{query:query},
            success:function(data)
            { 
                $('tbody').html(data);
                $('tbody').append(data.htmlresponse);
            }
        })
    }
 
    $('#search_filter').change(function(){
        $('#hidden_value').val($('#search_filter').val());
        var query = $('#hidden_value').val(); 
        load_data(query);
    });
     
});
