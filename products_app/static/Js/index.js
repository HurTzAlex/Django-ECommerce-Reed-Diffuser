// ดึงข้อมูลวันที่ปัจจุบัน
const currentDate = new Date();

// ดึงชื่อเดือน
const monthNames = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
];
const currentMonth = monthNames[currentDate.getMonth()];

// สร้างข้อความโปรโมชั่น ใช้ `` (ปุ่มเปลี่ยนภาษา)
const promotionText = `${currentMonth}`;

// แสดงข้อความในไฟล์ Html
document.getElementById('promotion').innerHTML = promotionText;

// Logo to Top
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

document.addEventListener("DOMContentLoaded", function () {
    

    // About, Promotion, Best-Seller and Products
    document.querySelectorAll('nav li a').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                const offset = 50;
                const targetPosition = targetElement.offsetTop - offset;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });


    // Footer Copyright
    const startYear = 2023;
    const currentYear = new Date().getFullYear();

    document.getElementById('startYear').innerText = startYear;
    document.getElementById('currentYear').innerText = currentYear;
});

// Social link
document.querySelectorAll('.detail-wrapper .icon').forEach(icon => {
    icon.addEventListener('click', function () {
        const platformId = this.id;
        let platformURL;
        switch (platformId) {
            case 'facebook':
                platformURL = 'https://www.facebook.com/AiiMoolek';
                break;
            case 'instagram':
                platformURL = 'https://www.instagram.com/nk_alex69';
                break;
            case 'tiktok':
                platformURL = 'https://www.tiktok.com/@nk_alex69';
                break;
            case 'linkedin':
                platformURL = 'https://www.linkedin.com/in/nattapong-khamhaengpol-9b138026a/';
                break;
            case 'github':
                platformURL = 'https://github.com/HurTzAlex';
                break;
            // เพิ่มเติมตามความต้องการ
        }
        window.open(platformURL, '_blank');
    });
});

// Contact link
document.querySelectorAll('.detail-wrapper-btm .icon').forEach(icon => {
    icon.addEventListener('click', function () {
        const platformId = this.id;
        let platformURL;
        switch (platformId) {
            case 'phone':
                platformURL = 'tel:+66923268999';
                break;
            case 'line':
                platformURL = 'https://line.me/ti/p/your-line-id';
                break;
            case 'email':
                platformURL = 'mailto:nattap0927@gmail.com';
                break;
            // เพิ่มเติมตามความต้องการ
        }
        window.open(platformURL, '_blank');
    });
});
