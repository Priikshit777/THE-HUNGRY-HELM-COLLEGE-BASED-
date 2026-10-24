# ⚓ The Hungry Helm — Backend API

Node.js + Express + MongoDB backend for the Bennett University campus food ordering system.

---

## Tech Stack

| Layer       | Technology                        |
|-------------|-----------------------------------|
| Runtime     | Node.js                           |
| Framework   | Express.js                        |
| Database    | MongoDB (via Mongoose)            |
| Auth        | JWT (jsonwebtoken) + bcryptjs     |
| Payments    | Razorpay                          |

---

## Project Structure

```
hungry-helm-backend/
├── config/
│   ├── db.js            — MongoDB connection
│   └── seed.js          — Seed outlets, menus & demo accounts
├── models/
│   ├── User.js          — Student + Staff accounts
│   ├── Outlet.js        — Outlets + embedded menu items
│   ├── Order.js         — Orders with status timeline
│   └── Payment.js       — Razorpay payment records
├── middleware/
│   ├── auth.js          — JWT protect, role guard, outlet ownership
│   └── error.js         — Global error handler
├── controllers/
│   ├── authController.js
│   ├── outletController.js
│   ├── orderController.js
│   └── paymentController.js
├── routes/
│   ├── auth.js
│   ├── outlets.js
│   ├── orders.js
│   └── payment.js
├── server.js            — App entry point
├── .env.example         — Environment variables template
└── package.json
```

---

## Setup

### 1. Install dependencies
```bash
npm install
```

### 2. Configure environment
```bash
cp .env.example .env
```
Edit `.env` and fill in:
- `MONGO_URI` — MongoDB Atlas connection string
- `JWT_SECRET` — any long random string (32+ characters)
- `RAZORPAY_KEY_ID` / `RAZORPAY_KEY_SECRET` — from Razorpay dashboard

### 3. Seed the database
```bash
npm run seed
```
This populates all 5 outlets with their full menus (exact data from script.js) and creates demo accounts.

### 4. Start the server
```bash
# Development (with auto-restart)
npm run dev

# Production
npm start
```

Server runs on `http://localhost:5000`

---

## Demo Credentials (after seeding)

| Role    | Email                           | Password   | Extra          |
|---------|---------------------------------|------------|----------------|
| Student | aryan.sharma@bennett.edu.in     | password   | —              |
| Staff   | staff.ik@bennett.edu.in         | staff123   | staffId: IK-STAFF-001  |
| Staff   | staff.hc@bennett.edu.in         | staff123   | staffId: HC-STAFF-001  |
| Staff   | staff.ss@bennett.edu.in         | staff123   | staffId: SS-STAFF-001  |
| Staff   | staff.sn@bennett.edu.in         | staff123   | staffId: SN-STAFF-001  |
| Staff   | staff.hs@bennett.edu.in         | staff123   | staffId: HS-STAFF-001  |

---

## API Reference

All endpoints are prefixed with `/api`.  
Protected routes require: `Authorization: Bearer <token>`

### Auth

| Method | Endpoint              | Auth | Description                     |
|--------|-----------------------|------|---------------------------------|
| POST   | /auth/register        | —    | Register new student            |
| POST   | /auth/login           | —    | Student login                   |
| POST   | /auth/staff-login     | —    | Staff login                     |
| GET    | /auth/me              | ✅   | Get current user                |

#### POST /auth/register
```json
{ "name": "Aryan Sharma", "email": "aryan@bennett.edu.in", "password": "mypass123" }
```

#### POST /auth/login
```json
{ "email": "aryan@bennett.edu.in", "password": "mypass123" }
```

#### POST /auth/staff-login
```json
{ "outletId": "ik", "staffId": "IK-STAFF-001", "password": "staff123" }
```

**Response (all login endpoints):**
```json
{
  "success": true,
  "token": "eyJhbGci...",
  "user": { "id": "...", "name": "Aryan Sharma", "email": "...", "role": "student" }
}
```

---

### Outlets

| Method  | Endpoint                            | Auth         | Description              |
|---------|-------------------------------------|--------------|--------------------------|
| GET     | /outlets                            | —            | All outlets + menus      |
| GET     | /outlets/:outletId                  | —            | Single outlet            |
| PATCH   | /outlets/:outletId/status           | Staff        | Open / busy / closed     |
| POST    | /outlets/:outletId/menu             | Staff        | Add menu item            |
| PATCH   | /outlets/:outletId/menu/:itemId     | Staff        | Edit item (price/stock)  |
| DELETE  | /outlets/:outletId/menu/:itemId     | Staff        | Remove item              |

#### PATCH /outlets/ik/status
```json
{ "status": "open" }   // "open" | "busy" | "closed"
```

#### POST /outlets/ik/menu  (Add Item modal)
```json
{
  "name": "Butter Chicken",
  "description": "Tomato cream gravy",
  "price": 150,
  "category": "Mains",
  "isVeg": false,
  "inStock": true
}
```

#### PATCH /outlets/ik/menu/:itemId  (toggle stock / edit price)
```json
{ "inStock": false }
// or
{ "price": 165 }
```

---

### Orders

| Method | Endpoint                          | Auth    | Description                     |
|--------|-----------------------------------|---------|---------------------------------|
| POST   | /orders                           | Student | Place order                     |
| GET    | /orders/my                        | Student | My orders (all statuses)        |
| GET    | /orders/outlet/:outletId          | Staff   | Live orders for outlet          |
| PATCH  | /orders/:id/status                | Staff   | Advance order status            |
| GET    | /orders/:id                       | Both    | Single order detail             |

#### POST /orders  (place order)
```json
{
  "outletId": "ik",
  "items": [
    { "itemId": "<mongo_id_of_menu_item>", "qty": 1 },
    { "itemId": "<mongo_id_of_menu_item>", "qty": 2 }
  ]
}
```

#### GET /orders/outlet/ik?status=incoming
Query params:
- `status` — filter by status: `incoming | preparing | ready | completed`
- `today=false` — include all-time orders (default: today only)

#### PATCH /orders/:id/status  (staff actions)
```json
{ "action": "accept" }    // incoming → preparing
{ "action": "ready" }     // preparing → ready
{ "action": "complete" }  // ready → completed
{ "action": "cancel" }    // → cancelled
```

---

### Payment

| Method | Endpoint                              | Auth    | Description                      |
|--------|---------------------------------------|---------|----------------------------------|
| POST   | /payment/create-order                 | Student | Create Razorpay order            |
| POST   | /payment/verify                       | Student | Verify payment signature         |
| GET    | /payment/history                      | Student | Full payment history             |
| GET    | /payment/outlet/:outletId/summary     | Staff   | Today's revenue + top items      |

---

## Connecting the Frontend (script.js)

Add this API helper at the top of `script.js`:

```javascript
const API = 'http://localhost:5000/api';
let authToken = localStorage.getItem('hhToken') || null;

async function apiCall(method, path, body = null) {
  const opts = {
    method,
    headers: {
      'Content-Type': 'application/json',
      ...(authToken ? { 'Authorization': `Bearer ${authToken}` } : {})
    }
  };
  if (body) opts.body = JSON.stringify(body);
  const res  = await fetch(API + path, opts);
  const data = await res.json();
  if (!res.ok) throw new Error(data.message || 'API error');
  return data;
}
```

### Replace loginStudent()
```javascript
async function loginStudent() {
  const email    = document.getElementById('sEmail').value.trim();
  const password = document.getElementById('sPass').value;
  try {
    const data = await apiCall('POST', '/auth/login', { email, password });
    authToken  = data.token;
    localStorage.setItem('hhToken', authToken);
    currentUser = {
      name:     data.user.name,
      email:    data.user.email,
      initials: data.user.name.split(' ').map(w => w[0]).join('').slice(0, 2)
    };
    // load outlets from DB instead of hardcoded array
    const { outlets } = await apiCall('GET', '/outlets');
    OUTLETS.length = 0;
    outlets.forEach(o => OUTLETS.push(mapOutlet(o))); // see mapOutlet() below
    // ... rest of your existing loginStudent logic
    navigate('home');
  } catch (err) { toast(err.message); }
}
```

### Replace loginStaff()
```javascript
async function loginStaff() {
  const outletId = document.getElementById('staffOutletSel').value;
  const staffId  = document.getElementById('staffId').value.trim();
  const password = document.getElementById('staffPass').value;
  try {
    const data = await apiCall('POST', '/auth/staff-login', { outletId, staffId, password });
    authToken  = data.token;
    localStorage.setItem('hhToken', authToken);
    currentStaff = { outlet: OUTLETS.find(o => o.id === outletId) };
    // ... rest of your existing loginStaff logic
  } catch (err) { toast(err.message); }
}
```

### Map DB outlet → UI outlet format
```javascript
function mapOutlet(o) {
  return {
    id:       o.outletId,
    name:     o.name,
    icon:     o.icon,
    cuisine:  o.cuisine,
    wait:     o.waitTime,
    status:   o.status,
    color:    o.color,
    dotColor: o.dotColor,
    cats:     ['All', ...o.categories],
    pos:      PORT_POSITIONS[o.outletId], // keep hardcoded map positions
    items:    o.menu.map(i => ({
      id:    i._id,       // use mongo _id as item id
      n:     i.name,
      d:     i.description,
      p:     i.price,
      c:     i.category,
      v:     i.isVeg,
      stock: i.inStock
    }))
  };
}
// Keep chart positions hardcoded (they're visual layout, not data)
const PORT_POSITIONS = {
  ik: { left:'20%', top:'35%' },
  hc: { left:'52%', top:'28%' },
  ss: { left:'30%', top:'72%' },
  sn: { left:'70%', top:'68%' },
  hs: { left:'76%', top:'38%' }
};
```

### Replace confirmOrder() — place order + payment
```javascript
async function confirmOrder() {
  const keys  = Object.keys(cart).filter(k => cart[k].qty > 0);
  const items = keys.map(k => ({ itemId: cart[k].mongoId, qty: cart[k].qty }));
  try {
    // 1. Create order in DB
    const { order } = await apiCall('POST', '/orders', { outletId: cartOutletId, items });

    // 2. Create Razorpay order
    const pay = await apiCall('POST', '/payment/create-order', { orderId: order._id });

    // 3. Open Razorpay checkout
    const rzp = new Razorpay({
      key:       pay.key,
      amount:    pay.amount,
      currency:  pay.currency,
      order_id:  pay.razorpayOrderId,
      name:      'The Hungry Helm',
      description: order.outletName,
      prefill:   pay.prefill,
      handler: async function(response) {
        // 4. Verify payment
        await apiCall('POST', '/payment/verify', {
          orderId:              order._id,
          razorpay_order_id:    response.razorpay_order_id,
          razorpay_payment_id:  response.razorpay_payment_id,
          razorpay_signature:   response.razorpay_signature
        });
        cart = {};
        closeModal('confirmModal');
        renderCartPanel();
        navigate('orders');
        renderOrdersPage();
        toast(`Order ${order.displayId} placed! 🎉`);
      }
    });
    rzp.open();
  } catch (err) { toast(err.message); }
}
```

### Load live orders (My Orders tab)
```javascript
async function renderOrdersPage() {
  const { orders } = await apiCall('GET', '/orders/my');
  // Map DB status to UI status (DB uses 'incoming', UI uses same)
  const active    = orders.filter(o => o.status !== 'completed' && o.status !== 'cancelled');
  const completed = orders.filter(o => o.status === 'completed');
  // ... render using your existing card HTML
}
```

### Staff: load live orders
```javascript
async function renderStaffOrders() {
  const outletId = currentStaff.outlet.id;
  const { orders } = await apiCall('GET', `/orders/outlet/${outletId}`);
  const incoming  = orders.filter(o => o.status === 'incoming');
  const inProg    = orders.filter(o => o.status === 'preparing' || o.status === 'ready');
  // ... render tickets using existing HTML
}
```

### Staff: advance order status
```javascript
async function staffAct(orderId, action) {
  // orderId here is the MongoDB _id (store it on the ticket element)
  try {
    await apiCall('PATCH', `/orders/${orderId}/status`, { action });
    renderStaffOrders();
    if (action === 'complete') toast('Order completed!');
  } catch (err) { toast(err.message); }
}
```

### Staff: toggle stock
```javascript
async function toggleStock(outletId, itemMongoId, el) {
  const item   = OUTLETS.find(o => o.id === outletId).items.find(i => i.id === itemMongoId);
  const newVal = !item.stock;
  try {
    await apiCall('PATCH', `/outlets/${outletId}/menu/${itemMongoId}`, { inStock: newVal });
    item.stock = newVal;
    el.classList.toggle('on');
    el.nextElementSibling.textContent = newVal ? 'In Stock' : 'Out';
    toast(`${item.n} → ${newVal ? 'available' : 'out of stock'}`);
  } catch (err) { toast(err.message); }
}
```

### Staff: reports tab
```javascript
async function loadReports() {
  const outletId = currentStaff.outlet.id;
  const { summary } = await apiCall('GET', `/payment/outlet/${outletId}/summary`);
  document.querySelector('#sc-done').textContent = summary.totalOrders;
  // render summary.topItems into the rpt-table
}
```

---

## Razorpay Checkout Setup

Add the Razorpay script to `index.html`:
```html
<script src="https://checkout.razorpay.com/v1/checkout.js"></script>
```
Use `rzp_test_*` keys while testing — no real money is charged.

---

## Environment Variables Reference

| Variable              | Required | Description                                      |
|-----------------------|----------|--------------------------------------------------|
| PORT                  | No       | Server port (default: 5000)                      |
| NODE_ENV              | No       | `development` or `production`                    |
| MONGO_URI             | **Yes**  | MongoDB Atlas connection string                  |
| JWT_SECRET            | **Yes**  | Secret for signing JWTs (32+ chars)              |
| JWT_EXPIRES_IN        | No       | Token expiry (default: 7d)                       |
| RAZORPAY_KEY_ID       | **Yes**  | From Razorpay dashboard                          |
| RAZORPAY_KEY_SECRET   | **Yes**  | From Razorpay dashboard                          |
| CLIENT_URL            | No       | Frontend origin for CORS (default: *)            |
