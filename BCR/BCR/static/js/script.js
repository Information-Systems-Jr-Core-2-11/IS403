var bannerOptions = ['banner-home-1.png', 
                     'banner-home-2.png', 
                     'banner-home-3.png', 
                     'banner-home-4.png'];
$('#random-banner').css({ 'background-image': 'url(https://codingitclassy.com/hosted-assets/hcr/Full_v1_0/img/' + bannerOptions[Math.floor(Math.random() * bannerOptions.length)] + ')'
});