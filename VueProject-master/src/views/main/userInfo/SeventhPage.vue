 <template>
     <div class="layout">
       <Layout>
         <Header>
           <Menu mode="horizontal" theme="dark" active-name="1">
             <div class="layout-logo">计算机网络</div>
             <div class="layout-nav">
               <MenuItem name="1" @click="submitForm('ruleForm')">
               <Icon type="ios-navigate"></Icon>
                 输入信息
              </MenuItem>
              <MenuItem name="2">
                <Icon type="ios-keypad"></Icon>
                结果显示
              </MenuItem>
              <MenuItem name="3">
                <Icon type="ios-analytics"></Icon>
                详细信息
              </MenuItem>
              <MenuItem name="4">
                <Icon type="ios-paper"></Icon>
                操作介绍
              </MenuItem>
            </div>
          </Menu>
        </Header>
        <Content :style="{padding: '0 50px'}">
          <Breadcrumb :style="{margin: '20px 0'}">
            <BreadcrumbItem>网络信息列表</BreadcrumbItem>
          </Breadcrumb>
          <Card>
             
            <div style="min-height: 200px;">
              <v-table
                is-horizontal-resize
                style="width:100%"
                :columns="columns"
                :table-data="tableData"
                row-hover-color="#eee"
                row-click-color="#edf7ff"
              ></v-table>
            </div>
           <!-- 分页 -->
<div class="pagination">
  <el-pagination
    background
    :current-page="pagination.currentPage"
    :page-sizes="[5, 10, 20, 40]"
    :page-size="pagination.pageSize"
    layout="total, sizes, prev, pager, next, jumper"
    :total="14"
    @size-change="handleSizeChange"
    @current-change="handleCurrentChange">
  </el-pagination>
</div> </Card>
        </Content>
        <Footer class="layout-footer-center"> © 作者：liuyang</Footer>
      </Layout>
    </div>
  </template>
  
  <script>
    export default {
      name: "table-main",
      data() {
        return {
        pagination: {
        currentPage: 1, //初始页
        pageSize: 5, //每页的数据
        start: 1,
        totalCount: 14 //总数据
      },
        tableData: [ ],
        columns: [
            {field: 'id', title: '主机01IP', width: 80, titleAlign: 'center', columnAlign: 'center',isResize:true},
            {field: 'createTime', title: '主机02IP', width: 80, titleAlign: 'center', columnAlign: 'center',isResize:true},
            {field: 'username', title: '主机03IP', width: 80, titleAlign: 'center', columnAlign: 'center',isResize:true},
            {field: 'phone', title: '外主机IP', width: 150, titleAlign: 'center', columnAlign: 'center',isResize:true},
            {field: 'email', title: '用户邮箱', width: 150, titleAlign: 'center', columnAlign: 'center',isResize:true},
            {field: 'zone', title: '其他信息', width: 280, titleAlign: 'center', columnAlign: 'center',isResize:true}
          ],
        navList:[
          {
            name:'/components/HelloWorld',navItem:'jiwangjiwang'
          }
          ],
        userList: [],
        listLoading: true,
        listQuery: {
           email: undefined,
           pageNum: 2,
           pageSize: 5
    },
        }
      },
      methods:{
        submitForm(formName){

        },
        handleSelect(key,keyPath){
          console.log(key,keyPath);
        },
            
        handleSizeChange(size) {
          this.pagination.pageSize = size;
          this.listQuery.pageSize = size;
          this.getUserList();
          console.log(this.pagination.pageSize) 
        },
    
        handleCurrentChange(currentPage) {
          this.pagination.currentPage = currentPage;
          this.listQuery.pageNum = currentPage;
          this.getUserList()
          console.log(this.pagination.currentPage); 
        },
    
        searchData() {
          this.listQuery.pageNum = 2;
          this.pagination.currentPage = 1;
          this.getUserList();
        },
    
        getUserList() {
          this.listLoading = true;
          getUserList(this.listQuery).then(response => {
          this.listLoading = false;
          if (response.status == 1) {
          this.userList = response.data.userList;
          this.pagination.totalCount = response.data.totalCount;
        } else {
          this.$confirm(response.message);
        }
      }).catch(error => {
          this.listLoading = false;
      })
    },
      },
      created() {
        //在created函数中使用axios的get请求向后台获取用户信息数据
        this.$ajax( 'http://localhost:8080/findAll',{
            start: (this.currentPage-1)*this.pageSize,
            pageSize: this.pageSize}
        ).then(res => {
          this.tableData = res.data;
          console.log(res);
        }).catch(function (error) {
          console.log(error);
        });
      }
    }
  </script>
  
  <style scoped>
    .layout{
      border: 1px solid #d7dde4;
      background: #f5f7f9;
      position: relative;
      border-radius: 4px;
      overflow: hidden;
      height: 100%;
    }
    .layout-logo{
      width: 100px;
      height: 30px;
      background: #5b6270;
      border-radius: 3px;
      float: left;
      position: relative;
      top: 15px;
      left: 20px;
      font-weight: bold;
      text-align: center;
      color: #49ffcc;
   }
   .layout-nav{
     width: 500px;
     margin: 0 auto;
     margin-right: 20px;
   }
   .layout-footer-center{
     text-align: center;
   }
 </style>
