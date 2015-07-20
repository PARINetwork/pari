$(function() {
    var recorder, mic, soundFile, filter, soundBlob, inProgress;
    var obj_id = "#" + $("input[name=obj_id]").val();

    SC.initialize({
	client_id: $("input[name=client_id]").val()
    });

    function interleave(leftChannel, rightChannel) {
	var length = leftChannel.length + rightChannel.length;
	var result = new Float32Array(length);
	var inputIndex = 0;
	for (var index = 0; index < length;) {
	    result[index++] = leftChannel[inputIndex];
	    result[index++] = rightChannel[inputIndex];
	    inputIndex++;
	}
	return result;
    }

    $("input.record").on("click", function() {
	if ($(this).val() === "Record") {
	    recorder = new p5.SoundRecorder();
	    mic = new p5.AudioIn();
	    soundFile = new p5.SoundFile();
	    mic.start();
	    recorder.setInput(mic);
	    recorder.record(soundFile);
	    $(this).val("Stop");
	} else {
	    mic.stop();
	    recorder.stop();
	    $(this).val("Record");
	}
    });
    $("input.play").on("click", function() {
	filter = new p5.Filter('highpass');
	soundFile.disconnect();
	filter.set(150, 0.1);
	soundFile.connect(filter);
	soundFile.play();
    });

    function downloadFile() {
	var filename = $("input[name=audio_title]").val().replace(" ", "-");
	p5.prototype.saveSound(soundFile, filename + '.wav');
	var leftChannel = soundFile.buffer.getChannelData(0);
	var rightChannel = soundFile.buffer.getChannelData(1);
	var interleaved = interleave(leftChannel, rightChannel);
	var buffer = new ArrayBuffer(44 + interleaved.length * 2);
	soundBlob = new Blob([buffer]);
    }

    $("input.download").on("click", function() {
	downloadFile();
    });

    $("input.upload").on("click", function(e) {
	var sectionName = $(this).parents("section").attr("id");
	var title, assetData;
	while (typeof soundBlob === "undefined") {
	    downloadFile();
	    setTimeout(function() { }, 500);
	}
	if (sectionName === "upload") {
	    title = $("input[type=file]").prop("files")[0].name;
	    assetData = $("input[type=file]").prop("files")[0];
	} else {
	    title = $("input[name=audio_title]").val();
	    assetData = soundBlob;
	}
	var fd = new FormData();
	fd.append('oauth_token', $("input[name=access_token]").val());
	fd.append('format','json');
	fd.append("track[title]", title);
	fd.append("track[asset_data]", assetData);

	if (!inProgress) {
	    $.ajax({
		url: 'https://api.soundcloud.com/v1/tracks',
		type: 'POST',
		data: fd,
		processData: false,
		contentType: false,
		xhr: function() {
		    inProgress = true;
		    var xhr = $.ajaxSettings.xhr();
		    xhr.upload.onprogress = function(e) {
			if(e.lengthComputable) {
			    var percent = Math.floor((e.loaded / e.total) * 100) + '%';
			    if ($(".progress").hasClass("hidden")) {
				$(".progress").removeClass("hidden").addClass("active");
			    }
			    $(".progress .bar").html(percent).css("width", percent);
			}
		    };
		    return xhr;
		}
	    }).done(function(e) {
		inProgress = false;
		$(".progress .bar").html('Upload Complete!');
		$(obj_id).val(e.id);
	    }).fail(function() {
		inProgress = false;
	    });
	}
	e.preventDefault();
    });
});
