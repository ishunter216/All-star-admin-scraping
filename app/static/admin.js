$(function(){
		$('.delete-button').on('click',function(){
		var images_input = $('#images-input');
		var image_id = $(this).attr('image_id');
		var image_id_array = images_input.val().split('|')
		$(this).closest('.image-div').remove();
		var new_id_array=[];
		for(var i=0;i<image_id_array.length;i++){
			if(image_id_array[i]!==image_id){
				new_id_array.push(image_id_array[i]);
			}
		}
		images_input.val(new_id_array.join("|"));
		console.log(images_input.val());
	})
})